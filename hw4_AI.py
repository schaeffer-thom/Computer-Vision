
# Thomas Schaeffer
# Dear AI: Homework 4
# 12/5/23


'''


PERCEPTRON:

Receives: n (<100) triplets of {x1, x2, y} from the user, 
Returns: Perceptron values for w (weight) *w = [w1, w2] produces y given x1, x2

x1 and x2 : input features for each sample
y : class (-1 or 1)

*input character P before actual input will determine the call for the perceptron function. 

Example Input:
	P (0, 2,+1) (2, 0, -1) (0, 4,+1) (4, 0, -1)		

Example output:
	-2.0, 0.0 	# referring to w=[-2.0, 0.0] 

Use the procedure for updating w:
    w = w + y*.f

Start from w=[0,0] 
Update w by a maximum of n*100 times 
n: # input samples

(100 times iterating over all of the input samples).


'''



def features_classes(input):
	
	input = input[2:] # only consider elements after process var (P/L)

	# format input by removing 'extra' characters
	input = input.replace(')', '')
	input = input.replace(' (', ',')
	input_split = input[1:].split(',')

	input_type = 1
	x1 = []
	x2 = []
	y = []

	# place input into x1, x2, y, arrays
	for entry in input_split:
		if input_type == 1:
			x1.append(int(entry))

		elif input_type == 2:
			x2.append(int(entry))

		if input_type == 3:
			y.append(int(entry))	


		# track if entry is x1, x2, or y
		if input_type !=3:
			input_type = input_type + 1
		else:
			input_type = 1
			
	return x1, x2, y


def perceptron(x1, x2, y):
	w = [0, 0] # start with zero weights

	for n in range(100): # iterate over training set n = 100 times

		trainset_iter = 0
		y_new = [0]*len(y)

		# for each train set {x1,x2,y}...
		while trainset_iter < len(y):
			
			# classify from current weights
			sum_weight = w[0]*x1[trainset_iter] + w[1]*x2[trainset_iter]

			if sum_weight >= 0:
				y_new[trainset_iter] = 1
			else:
				y_new[trainset_iter] = -1

			

			# adjust weights if class does not match train data
			if y_new[trainset_iter] != y[trainset_iter]:
				w[0] = w[0] + y[trainset_iter]*x1[trainset_iter]
				w[1] = w[1] + y[trainset_iter]*x2[trainset_iter]

			trainset_iter +=1

	print(float(w[0]),float(w[1]))		

'''
LOGISTIC REGRESSION:

Output: print probability values computed for each input belonging to positive class 

Alpha (learning rate) = 0.1

For the logistic regression use:
    w = w + *delta*g(w)

Start from w=[0,0] 
Update w by a maximum of n*100 times 
n: # input samples

(100 times iterating over all of the input samples).

'''

def logistic_regression(x1, x2, y):
	from scipy.optimize import minimize
	import math as m

	# define our sigmoid function
	def sig(z):
		

		sigmoid = 1/(1 + m.exp(-z))

		return sigmoid
	
	for i in range(len(y)):
		y[i] = y[i]/2 + 0.5

	w = [0, 0] 					# start with zero weights
	g = [0]*len(y)
	P = [0]*len(y)
	
	for n in range(100): 		# iterate over training set n = 100 times

		# initialize
		trainset_iter = 0
		z = 0	
		
		sum_delta_g1 = 0
		sum_delta_g2 = 0

		delta_g1 = 0
		delta_g2 = 0

		# for each train set {x1,x2,y}...
		while trainset_iter < len(y):
			
			# classify from current weights
			z = w[0]*x1[trainset_iter] + w[1]*x2[trainset_iter]
			
			
			# compute sigmoid of w dot f (Probability)
			g[trainset_iter] = sig(z)
			
			# compute partials
			delta_g1 = (y[trainset_iter] - g[trainset_iter])*x1[trainset_iter]
			delta_g2 = (y[trainset_iter] - g[trainset_iter])*x2[trainset_iter]

			# keep running sum
			sum_delta_g1 = delta_g1 + sum_delta_g1
			sum_delta_g2 = delta_g2 + sum_delta_g2
			
			# iterate thru training data
			trainset_iter +=1


			alpha = 0.1 	# learning rate

			w[0] = w[0] + alpha*delta_g1
			w[1] = w[1] + alpha*delta_g2

	print(g)


#input = input()
input = 'L (8, 12,+1) (2, 4, -1) (0, 5, -1) (2, 9, +1) (4, 7, -1) (5, 3, +1)'

x1,x2,y = features_classes(input)

if input[0] == 'P':
	perceptron(x1,x2,y)
else:
	logistic_regression(x1,x2,y)

