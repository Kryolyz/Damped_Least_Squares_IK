# Damped_Least_Squares_IK
A Python 2D implementation of the Damped Least Squares Inverse Kinematics algorithm for a single arm with arbitrarily many joints. It's a numerical method to move a robotic arm to a target position. The key feature is the damping constant which lets the user intuitively manipulate the step size and prevent singularities in the jacobi-matrix from making the arm swing around wildly. Properly determining the damping constant is crucial for good perfomance. Complex arms require a higher damping constant. In case you are interested in using and/or improving the code, feel free to copy it and add adaptive damping as suggested in the paper in the References folder.


# References
The main paper is in the References folder. It's a review paper that compares the strenghts and weaknesses of several numerical inverse kinematics algorithms. Feel free to copy and change my code to try out different methods.
