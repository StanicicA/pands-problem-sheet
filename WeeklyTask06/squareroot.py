#Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

#You should create a function called <tt>sqrt</tt> that does this.

#I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).

#I suggest that you look at the newton method at estimating square roots.
#Please enter a positive number: 14.5
#The square root of 14.5 is approx. 3.8.
#Resource:https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N.
#Author: Andrea Stanicic

input = float (input("Please enter a positive number:"))
print (input)

#Function to return the square root of a number using Newtons method 
 double squareRoot(double n, float l)
{
    # Assuming the sqrt of n as n only
    double x = n;
 
    // The closed guess will be stored in the root
    double root;
 
    // To count the number of iterations
    int count = 0;
 
    while (1) {
        count++;
 
        // Calculate more closed x
        root = 0.5 * (x + (n / x));
 
        // Check for closeness
        if (abs(root - x) < l)
            break;
 
        // Update root
        x = root;
    }
 
    return root;
}
 
// Driver code
int main()
{
    double n = 327;
    float l = 0.00001;
 
    cout << squareRoot(n, l);
 
    return 0;
}