__all__ = ['NW_kerreg_1d']

import numpy as np
from ._onedim import _kernelregression_1d_base

def NW_kerreg_1d(x, y, bandwidth, kernel="rectangular", weight=None, delay_input_processing=False):
	allowed_kernels = ["rectangular", "triangular", "exponential"]
	NW_1d_dict = {"rectangular": _NW_1d_rectangular_fast, "triangular": _NW_1d_triangular_fast, "exponential": _NW_1d_exponential}
	NW_1d_dict_advanced = {"rectangular_nstable": _NW_1d_rectangular_numericallystable, "triangular_nstable": _NW_1d_triangular_numericallystable}
	NW_1d_dict.update(NW_1d_dict_advanced)
	
	if len(allowed_kernels) == 2:
		allowed_kernels_string = f'''"{allowed_kernels[0]}" and "{allowed_kernels[1]}"'''
	elif len(allowed_kernels) > 2:
		allowed_kernels_string = f'''"{'", "'.join(allowed_kernels[:-1])}", and "{allowed_kernels[-1]}"'''
	
	if kernel not in allowed_kernels:
		raise(ValueError("Invalid option for 'kernel' parameter. Possible options are {allowed_kernels_string}."))
	
	#TODO: input sanitation
	
	to_return = NW_1d_dict[kernel](x, y, bandwidth, weight, delay_input_processing)
	to_return.kernel_name = kernel
	return to_return

class _NW_1d_rectangular_fast(_kernelregression_1d_base):
	_variable_bandwidth_allowed = True
	
	def process_input(self):
		self.breakpoints = np.concatenate((self.x - self.bandwidth, self.x + self.bandwidth))
		
		Nr_terms = 0.5*self.weight*self.y/self.bandwidth
		Nr_terms = np.concatenate((Nr_terms, -Nr_terms))
		Dr_terms = 0.5*self.weight/self.bandwidth
		Dr_terms = np.concatenate((Dr_terms, -Dr_terms))
		
		del self.x, self.y, self.weight, self.bandwidth
		
		sort_indices = np.argsort(self.breakpoints)
		self.breakpoints = self.breakpoints[sort_indices]
		Nr_terms = Nr_terms[sort_indices]
		Dr_terms = Dr_terms[sort_indices]
		
		self.Nr_atbreakpoints = np.cumsum(Nr_terms)
		self.Dr_atbreakpoints = np.cumsum(Dr_terms)
	
	def evaluate(self, q, return_Nr_Dr = False):
		index = np.searchsorted(self.breakpoints, q, side='right') #right => [)
		Nr = np.where(index > 0, self.Nr_atbreakpoints[index-1], 0.)
		Dr = np.where(index > 0, self.Dr_atbreakpoints[index-1], 0.)
		
		if return_Nr_Dr:
			return Nr, Dr
		else:
			return Nr/Dr

class _NW_1d_triangular_fast(_kernelregression_1d_base):
	_variable_bandwidth_allowed = True
	
	def process_input(self):
		ones = np.ones(self.x.shape)
		zeros = np.zeros(self.x.shape)
		
		self.breakpoints = np.concatenate((self.x-self.bandwidth, self.x, self.x+self.bandwidth))
		Nr_aux_terms = self.weight*self.y/self.bandwidth**2.
		Dr_aux_terms = self.weight/self.bandwidth**2.
		
		del self.x, self.y, self.weight, self.bandwidth
		
		breakpoints_isleft = np.concatenate(ones, ones, zeros)
		breakpoints_isright = np.concatenate(zeros, ones, ones)
		
		Nr_aux_left = np.concatenate((Nr_aux_terms, -Nr_aux_terms, zeros))
		Nr_aux_right = np.concatenate((zeros, Nr_aux_terms, -Nr_aux_terms))
		
		Dr_aux_left = np.concatenate((Dr_aux_terms, -Dr_aux_terms, zeros))
		Dr_aux_right = np.concatenate((zeros, Dr_aux_terms, -Dr_aux_terms))
		
		sort_indices = np.argsort(self.breakpoints)
		self.breakpoints = self.breakpoints[sort_indices]
		breakpoints_isleft = breakpoints_isleft[sort_indices]
		breakpoints_isright = breakpoints_isright[sort_indices]
		
		Nr_aux_cumsum_left = np.cumsum(Nr_aux_left[sort_indices])
		Nr_aux_cumsum_right = np.cumsum(Nr_aux_right[sort_indices])
		
		Dr_aux_cumsum_left = np.cumsum(Dr_aux_left[sort_indices])
		Dr_aux_cumsum_right = np.cumsum(Dr_aux_right[sort_indices])
		
		dNr_atbreakpoints = np.zeros(self.breakpoints.shape)
		dNr_atbreakpoints[1:] = breakpoints_isleft[1:] * Nr_aux_cumsum_left[:-1] * np.diff(self.breakpoints) \
						- breakpoints_isright[1:] * Nr_aux_cumsum_right[:-1] * np.diff(self.breakpoints)
		
		dDr_atbreakpoints = np.zeros(self.breakpoints.shape)
		dDr_atbreakpoints[1:] = breakpoints_isleft[1:] * Dr_aux_cumsum_left[:-1] * np.diff(self.breakpoints) \
						- breakpoints_isright[1:] * Dr_aux_cumsum_right[:-1] * np.diff(self.breakpoints)
		
		self.Nr_atbreakpoints = np.cumsum(dNr_atbreakpoints)
		self.Dr_atbreakpoints = np.cumsum(dDr_atbreakpoints)
		
		self.Nr_aux_cumsum_leftminusright = self.Nr_aux_cumsum_left - self.Nr_aux_cumsum_right
		self.Dr_aux_cumsum_leftminusright = self.Dr_aux_cumsum_left - self.Dr_aux_cumsum_right
	
	def evaluate(self, q, return_Nr_Dr = False):
		index = np.searchsorted(self.breakpoints, q, side='right') #right => [)
		Nr = np.where(index > 0, self.Nr_atbreakpoints[index-1] \
								+ self.Nr_aux_cumsum_leftminusright[index-1] * (self.breakpoints[index] - self.breakpoints[index-1]) \
								, 0.)
		Dr = np.where(index > 0, self.Dr_atbreakpoints[index-1] \
								+ self.Dr_aux_cumsum_leftminusright[index-1] * (self.breakpoints[index] - self.breakpoints[index-1]) \
								, 0.)
		
		if return_Nr_Dr:
			return Nr, Dr
		else:
			return Nr/Dr

class _NW_1d_exponential(_kernelregression_1d_base):
	_variable_bandwidth_allowed = False
	
	def process_input(self):
		self.Nr_cumsum_left = self.weight*self.y
		self.Dr_cumsum_left = self.weight
		del self.y, self.weight
		
		sort_indices = np.argsort(self.x)
		self.x = self.x[sort_indices]
		self.Nr_cumsum_left = self.Nr_cumsum_left[sort_indices]
		self.Dr_cumsum_left = self.Dr_cumsum_left[sort_indices]
		
		self.Nr_cumsum_right = np.copy(self.Nr_cumsum_left)
		self.Dr_cumsum_right = np.copy(self.Dr_cumsum_left)
		
		kernel_dropfactor = np.exp(-np.diff(self.x)/self.bandwidth)
		
		for i in range(self.x.size-1):
			self.Nr_cumsum_left[i+1] += self.Nr_aux_left[i]*kernel_dropfactor[i]
			self.Dr_cumsum_left[i+1] += self.Dr_aux_left[i]*kernel_dropfactor[i]
			
			self.Nr_cumsum_right[-2-i] += self.Nr_aux_cumsum_right[-1-i]*kernel_dropfactor[-1-i]
			self.Dr_cumsum_right[-2-i] += self.Dr_aux_cumsum_right[-1-i]*kernel_dropfactor[-1-i]
	
	def evaluate(self, q, return_Nr_Dr = False):
		index = np.searchsorted(self.x, q, side='right') #side doesn't matter
		
		tmp1 = np.where(index == 0, -np.inf, self.x[index-1] - q)
		tmp2 = np.where(index == self.x.size, -np.inf, q - self.x[index-self.x.size])
		
		Nr = self.Nr_aux_cumsum_left[index-1]*np.exp(tmp1) + self.Nr_aux_cumsum_right[index-self.x.size]*np.exp(tmp2)
		Dr = self.Dr_aux_cumsum_left[index-1]*np.exp(tmp1) + self.Dr_aux_cumsum_right[index-self.x.size]*np.exp(tmp2)
		
		if return_Nr_Dr:
			return Nr, Dr
		else:
			return Nr/Dr

class _NW_1d_rectangular_numericallystable(_kernelregression_1d_base):
	_variable_bandwidth_allowed = True
	
	def process_input(self):
		sort_indices = np.argsort(self.x)
		self.x = self.x[sort_indices]
		self.y = self.y[sort_indices]
		self.weight = self.weight[sort_indices]
		if not np.issubdtype(type(self.bandwidth), np.number):
			self.bandwidth = self.bandwidth[sort_indices]
		
		self.window_start = self.x - self.bandwidth
		self.window_end = self.x + self.bandwidth
		
		#TODO: assert that start and end are sorted
		
		self.Nr_tree = [0.5*self.weight*self.y/self.bandwidth]
		self.Dr_tree = [0.5*self.weight/self.bandwidth]
		
		while self.Nr_tree[-1].size > 1:
			self.Nr_tree.append(np.copy(self.Nr_tree[-1][0::2]))
			self.Nr_tree[-1][:self.Nr_tree[-2].size//2] += self.Nr_tree[-2][1::2]
			
			self.Dr_tree.append(np.copy(self.Dr_tree[-1][0::2]))
			self.Dr_tree[-1][:self.Dr_tree[-2].size//2] += self.Dr_tree[-2][1::2]
	
	def evaluate(self, q, return_Nr_Dr = False):
		Nr = np.zeros_like(q)
		Dr = np.zeros_like(q)
			
		from_index = np.searchsorted(self.window_end, q, side='right') #right => )
		to_index = np.searchsorted(self.window_start, q, side='right') #right => [
		
		# To keep from_index from going out of bound #################
		to_index = np.where(to_index > from_index, to_index, 0)
		from_index = np.where(to_index > 0, from_index, 0)
		##############################################################
		
		for i in range(len(self.Nr_tree)):
			is_nonempty = (to_index > from_index)
			include_first = np.logical_and(is_nonempty, from_index%2 == 1)
			include_last = np.logical_and(is_nonempty, to_index%2 == 1)
			
			Nr += np.where(include_first, self.Nr_tree[i][from_index], 0.)
			Nr += np.where(include_last, self.Nr_tree[i][to_index-1], 0.)
			
			Dr += np.where(include_first, self.Dr_tree[i][from_index], 0.)
			Dr += np.where(include_last, self.Dr_tree[i][to_index-1], 0.)
			
			from_index = (from_index+1)//2
			to_index //= 2
			
			to_index = np.where(to_index > from_index, to_index, 0)
			from_index = np.where(to_index > 0, from_index, 0)
		
		if return_Nr_Dr:
			return Nr, Dr
		else:
			return Nr/Dr

class _NW_1d_triangular_numericallystable(_kernelregression_1d_base):
	_variable_bandwidth_allowed = True
	
	def process_input(self):
		sort_indices = np.argsort(self.x)
		self.x = self.x[sort_indices]
		self.y = self.y[sort_indices]
		self.weight = self.weight[sort_indices]
		if not np.issubdtype(type(self.bandwidth), np.number):
			self.bandwidth = self.bandwidth[sort_indices]
		
		self.window_start = self.x - self.bandwidth
		self.window_end = self.x + self.bandwidth
		
		#TODO: assert that start and end are sorted
		
		self.min_xplusb_tree = [self.x+self.bandwidth]
		self.max_xminusb_tree = [self.x-self.bandwidth]
		
		self.Nr_aux_tree = [(self.weight*self.y)/(self.bandwidth**2.)]
		self.Dr_aux_tree = [self.weight/(self.bandwidth**2.)]
		
		self.Nr_right_tree = [np.zeros_like(self.Nr_aux_tree[0])]
		self.Dr_right_tree = [np.zeros_like(self.Dr_aux_tree[0])]
		
		self.Nr_left_tree = [np.zeros_like(self.Nr_aux_tree[0])]
		self.Dr_left_tree = [np.zeros_like(self.Dr_aux_tree[0])]
		
		while self.Nr_aux_tree[-1].size > 1:
			_size = self.Nr_aux_tree[-1].size
			
			self.min_xplusb_tree.append(np.copy(self.min_xplusb_tree[-1][0::2]))
			
			self.max_xminusb_tree.append(np.copy(self.max_xminusb_tree[-1][0::2]))
			self.max_xminusb_tree[-1][:_size//2] = self.max_xminusb_tree[-2][1::2]
			
			self.Nr_aux_tree.append(np.copy(self.Nr_aux_tree[-1][0::2]))
			self.Nr_aux_tree[-1][:_size//2] += self.Nr_aux_tree[-2][1::2]
			
			self.Dr_aux_tree.append(np.copy(self.Dr_aux_tree[-1][0::2]))
			self.Dr_aux_tree[-1][:_size//2] += self.Dr_aux_tree[-2][1::2]
			
			self.Nr_right_tree.append(np.copy(self.Nr_right_tree[-1][0::2]))
			self.Nr_right_tree[-1][:_size//2] += self.Nr_right_tree[-2][1::2]
			self.Nr_right_tree[-1][:_size//2] += self.Nr_aux_tree[-2][1::2] * (self.min_xplusb_tree[-2][1::2] - self.min_xplusb_tree[-1][:_size//2])
			
			self.Dr_right_tree.append(np.copy(self.Dr_right_tree[-1][0::2]))
			self.Dr_right_tree[-1][:_size//2] += self.Dr_right_tree[-2][1::2]
			self.Dr_right_tree[-1][:_size//2] += self.Dr_aux_tree[-2][1::2] * (self.min_xplusb_tree[-2][1::2] - self.min_xplusb_tree[-1][:_size//2])
			
			self.Nr_left_tree.append(np.copy(self.Nr_left_tree[-1][0::2]))
			self.Nr_left_tree[-1][:_size//2] += self.Nr_left_tree[-2][1::2]
			self.Nr_left_tree[-1] += self.Nr_aux_tree[-2][0::2] * (self.max_xminusb_tree[-1] - self.max_xminusb_tree[-2][0::2])
			
			self.Dr_left_tree.append(np.copy(self.Dr_left_tree[-1][0::2]))
			self.Dr_left_tree[-1][:_size//2] += self.Dr_left_tree[-2][1::2]
			self.Dr_left_tree[-1] += self.Dr_aux_tree[-2][0::2] * (self.max_xminusb_tree[-1] - self.max_xminusb_tree[-2][0::2])
	
	def evaluate(self, q, return_Nr_Dr):
		Nr = np.zeros_like(q)
		Dr = np.zeros_like(q)
		
		right_from_index = np.searchsorted(self.window_end, q, side='right') #right => )
		right_to_index = np.searchsorted(self.x, q, side='right') #right => [
		
		left_from_index = right_to_index #np.searchsorted(self.x, q, side='right')  #right => )
		left_to_index = np.searchsorted(self.window_start, q, side='right')  #right => [
		
		# To keep from_index from going out of bound #################
		right_to_index = np.where(right_to_index > right_from_index, right_to_index, 0)
		right_from_index = np.where(right_to_index > 0, right_from_index, 0)
		
		left_to_index = np.where(left_to_index > left_from_index, left_to_index, 0)
		left_from_index = np.where(left_to_index > 0, left_from_index, 0)
		##############################################################
		
		print(len(self.Nr_aux_tree))
		for i in range(len(self.Nr_aux_tree)):
			print(i)
			is_nonempty = (right_to_index > right_from_index)
			include_first = np.logical_and(is_nonempty, right_from_index%2 == 1)
			include_last = np.logical_and(is_nonempty, right_to_index%2 == 1)
			
			Nr += np.where(include_first, self.Nr_right_tree[i][right_from_index] + self.Nr_aux_tree[i][right_from_index] * (self.min_xplusb_tree[i][right_from_index] - q), 0.)
			Nr += np.where(include_last, self.Nr_right_tree[i][right_to_index-1] + self.Nr_aux_tree[i][right_to_index-1] * (self.min_xplusb_tree[i][right_to_index-1] - q), 0.)
			
			Dr += np.where(include_first, self.Dr_right_tree[i][right_from_index] + self.Dr_aux_tree[i][right_from_index] * (self.min_xplusb_tree[i][right_from_index] - q), 0.)
			Dr += np.where(include_last, self.Dr_right_tree[i][right_to_index-1] + self.Dr_aux_tree[i][right_to_index-1] * (self.min_xplusb_tree[i][right_to_index-1] - q), 0.)
			
			is_nonempty = (left_to_index > left_from_index)
			include_first = np.logical_and(is_nonempty, left_from_index%2 == 1)
			include_last = np.logical_and(is_nonempty, left_to_index%2 == 1)
			
			Nr += np.where(include_first, self.Nr_left_tree[i][left_from_index] + self.Nr_aux_tree[i][left_from_index] * (q - self.max_xminusb_tree[i][left_from_index]), 0.)
			Nr += np.where(include_last, self.Nr_left_tree[i][left_to_index-1] + self.Nr_aux_tree[i][left_to_index-1] * (q - self.max_xminusb_tree[i][left_to_index-1]), 0.)
			
			Dr += np.where(include_first, self.Dr_left_tree[i][left_from_index] + self.Dr_aux_tree[i][left_from_index] * (q - self.max_xminusb_tree[i][left_from_index]), 0.)
			Dr += np.where(include_last, self.Dr_left_tree[i][left_to_index-1] + self.Dr_aux_tree[i][left_to_index-1] * (q - self.max_xminusb_tree[i][left_to_index-1]), 0.)
			
			right_from_index = (right_from_index+1)//2
			right_to_index //= 2
			
			left_from_index = (left_from_index+1)//2
			left_to_index //= 2
			
			# To keep from_index from going out of bound #################
			right_to_index = np.where(right_to_index > right_from_index, right_to_index, 0)
			right_from_index = np.where(right_to_index > 0, right_from_index, 0)
			
			left_to_index = np.where(left_to_index > left_from_index, left_to_index, 0)
			left_from_index = np.where(left_to_index > 0, left_from_index, 0)
			##############################################################
			
			if np.all(right_to_index == 0) and np.all(left_to_index == 0):
				break
		
		if return_Nr_Dr:
			return Nr, Dr
		else:
			return Nr/Dr
