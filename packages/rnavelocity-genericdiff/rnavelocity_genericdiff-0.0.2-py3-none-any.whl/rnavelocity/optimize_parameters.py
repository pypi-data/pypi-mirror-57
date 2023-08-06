
# Performs optimization of the RNA velocity
# equation

import numpy as np
import random
import sys
# sys.path.append('../')
from genericdiff import *
from multiprocessing import Pool

from functions import calc_u as u_t
from functions import calc_s as s_t



###########
# Optimization
###########

def calc_total_loss_and_der_across_cells(alpha, gamma, u_0, s_0, \
	t_curr_allcells, u_t_actual_allcells, s_t_actual_allcells, jp_object, wrt=1):
	'''
	Calculate the loss and derivative
	'''

	total_cells = len(t_curr_allcells)
	loss_der_wrt_all_cells = np.empty(total_cells)
	loss_val_all_cells = np.empty(total_cells)
	
	# Loop through each cell and calculate the loss
	for i in range(len(t_curr_allcells)):
		t_curr = t_curr_allcells[i]
		u_t_actual = u_t_actual_allcells[i]
		s_t_actual = s_t_actual_allcells[i]


		# Define the input for the loss function
		inputs = [alpha, gamma, u_0, s_0, t_curr, u_t_actual, s_t_actual]
		jp_matrix_der = jp_object.partial_ders(wrt=wrt, inputs=inputs)
		jp_matrix_val = jp_object.partial_vals(wrt=wrt, inputs=inputs)


		# Get the loss function value, and derivative given the inputs
		loss_der_wrt = jp_matrix_der[0][0] # wrt is the index of variable of interest, alpha is 0, gamma is 1
		loss_val = jp_matrix_val[0][0] 

		# print(loss_val, loss_der_wrt)

		# Store the loss function and derivatives for each cell
		loss_der_wrt_all_cells[i] = loss_der_wrt
		loss_val_all_cells[i] = loss_val

	loss_sum = np.sum(loss_val_all_cells) / total_cells
	loss_der_sum = np.sum(loss_der_wrt_all_cells) / total_cells

	
	return loss_sum, loss_der_sum



def optimize_gamma(alpha, gamma, u_0, s_0, t_curr_allcells, u_t_actual_allcells, \
	s_t_actual_allcells, jp_object, learning_rate = 0.0001):
	'''
	Function to optimize the gamma value
	across all cells
	'''

	loss_val_sum, loss_der_gamma_sum = calc_total_loss_and_der_across_cells(alpha, gamma, u_0, s_0, \
	t_curr_allcells, u_t_actual_allcells, s_t_actual_allcells, jp_object, wrt=1)


	curr_gamma = gamma
	iterations = 0
	iterations_cutoff = 30


	while True and iterations < iterations_cutoff:
		new_gamma = curr_gamma - learning_rate * float(loss_val_sum / loss_der_gamma_sum) # Newton root finding
		# new_gamma = curr_gamma - learning_rate * loss_der_gamma_sum # Gradient descent
		# print("gamma:", new_gamma)

		# We reoptimize for gamma if the number becomes negative
		# by randomly selecting a new gamma for optimzation
		if new_gamma <= 0 :
			new_gamma = random.random()


		loss_val_sum, loss_der_gamma_sum = calc_total_loss_and_der_across_cells(alpha, new_gamma, u_0, s_0, \
		t_curr_allcells, u_t_actual_allcells, s_t_actual_allcells, jp_object, wrt=1)

		# print(loss_val_sum, loss_der_gamma_sum)

		curr_gamma = new_gamma

		if(abs(loss_der_gamma_sum) < 10 **(-8)):
			break

		iterations += 1

	return curr_gamma



def optimize_alpha(alpha, gamma, u_0, s_0, t_curr_allcells, u_t_actual_allcells, \
	s_t_actual_allcells, jp_object, learning_rate = 0.0001):
	'''
	Function to optimize the alpha value
	across all cells
	'''

	loss_val_sum, loss_der_alpha_sum = calc_total_loss_and_der_across_cells(alpha, gamma, u_0, s_0, \
	t_curr_allcells, u_t_actual_allcells, s_t_actual_allcells, jp_object, wrt=0)


	curr_alpha = alpha
	iterations = 0
	iterations_cutoff = 30


	while True and iterations < iterations_cutoff:
		new_alpha = curr_alpha - learning_rate * float(loss_val_sum / loss_der_alpha_sum) # newton root finding
		# new_alpha = curr_alpha - learning_rate * loss_der_alpha_sum # gradient descent

		# We reoptimize for gamma if the number becomes negative
		# by randomly selecting a new alpha for optimzation
		if new_alpha <= 0 :
			new_alpha = random.random()


		loss_val_sum, loss_der_alpha_sum = calc_total_loss_and_der_across_cells(new_alpha, gamma, u_0, s_0, \
		t_curr_allcells, u_t_actual_allcells, s_t_actual_allcells, jp_object, wrt=0)

		curr_alpha = new_alpha

		if(abs(loss_der_alpha_sum) < 10 **(-8)):
			break

		previous_error = loss_val_sum
		iterations += 1

	return curr_alpha



def optimize_gene(data, initial_cell_index, alpha_vals, gamma_vals, time_cell, jp_object, curr_gene_idx):
	print("Optimizing gene number:", curr_gene_idx)

	# try:
	iterations = 0
	iterations_cutoff = 2
	s_0 = data[0][curr_gene_idx][initial_cell_index]
	u_0 = data[1][curr_gene_idx][initial_cell_index]
	alpha = alpha_vals[curr_gene_idx]
	gamma = gamma_vals[curr_gene_idx]


	t_curr = time_cell
	u_t_actual = data[0][curr_gene_idx]
	s_t_actual = data[1][curr_gene_idx]


	new_alpha = alpha
	new_gamma = gamma
	while True and iterations < iterations_cutoff:
		# Alternating optimization between alpha and gamma
		print("Iteration:", iterations)
		new_gamma = optimize_gamma(new_alpha, new_gamma, u_0, s_0, t_curr, u_t_actual, s_t_actual, jp_object)
		new_alpha = optimize_alpha(new_alpha, new_gamma, u_0, s_0, t_curr, u_t_actual, s_t_actual, jp_object)
		
		iterations += 1


	return curr_gene_idx, new_alpha, new_gamma

	# except:
	# 	# Return NA if there's an error during the run
	# 	return curr_gene_idx, "NA", "NA"


def optimize_gene_parallel(data, initial_cell_index, alpha_vals, gamma_vals, time_cell, jp_object, geneidx):
	print("apple")
	# [data, initial_cell_index, alpha_vals, gamma_vals, time_cell, jp_object, geneidx] = input_data
	return optimize_gene(data, initial_cell_index, alpha_vals, gamma_vals, time_cell, jp_object, geneidx)



def overall_optimization(input_pickle_file="processed_data/norm_filtered_cells.scaled.pickle", \
	cell_order_file="output/cell_order.final.txt", \
	output_parameter_file="output/optimized_gene_parameters.txt", \
	num_processes=4):

	# Read data in from pickle file
	data = np.load(input_pickle_file, allow_pickle=True)
	num_cells = data.shape[2]
	num_genes = data.shape[1]


	# Randomize the time values (Time values are in per 10^6 scale)
	time_cell = [ x / 1000000 for x in range(num_cells)]

	# Set seed for 
	random.seed(1234)

	# Shuffle the time values between cells
	random.shuffle(time_cell)

	# Read in the graph of the cell order
	f = open(cell_order_file, "r")
	for line in f:
		order = line.strip().split(",")
	f.close()
	idx = [int(float(i)) for i in order]



	# Identify the index of the initial cell
	initial_cell_index = idx[0]


	# Randomize the alpha and gamma values
	# for each gene
	alpha_vals = [random.random() for i in range(num_genes)]
	gamma_vals = [random.random() for i in range(num_genes)]



	# Euclidean distance lambda function
	euclidean_distance = lambda u_t, s_t, u_t_actual, s_t_actual: sqrt((u_t - u_t_actual)**2 + (s_t - s_t_actual)**2)


	# Now combine them into final function that makes explicit what are variables (these can be your differentiating variables of interest but also your variable inputs):
	combined = lambda alpha, gamma, u_0, s_0, t_curr, u_t_actual, s_t_actual:\
	euclidean_distance(u_t(alpha, u_0, t_curr), s_t(alpha, gamma, u_0, s_0, t_curr), u_t_actual, s_t_actual)


	# Then make a jacobian product class
	jp_object = JacobianProduct([combined])


	# Generate data matrix of parameter
	input_parallel = []

	for i in range(4):
		input_parameters = (data, initial_cell_index, alpha_vals, gamma_vals, time_cell, jp_object, i)
		input_parallel.append(input_parameters)

	# print(input_parallel)

	# Perform multi-processing of the run
	# number_proc = num_processes
	# pool = Pool(processes = number_proc)
	# result = pool.map(optimize_gene_parallel, input_parallel)
	# # result = pool.map(optimize_gene, range(num_genes))

	for i in range(num_genes):
		optimize_gene(data, initial_cell_index, alpha_vals, gamma_vals, time_cell, jp_object, i)	


	# Print optimized parameters to output file
	output = open(output_parameter_file, "w")
	for result_line in result:
		output.write("\t".join(map(str, result_line)) + "\n")
		print(result_line)
	output.close()



if __name__ == "__main__":
	overall_optimization()


