#!/bin/bash

# Define the radius
radius=5

# Define the value of Pi
pi=3.14159

# Calculate the volume using bc for floating-point arithmetic
volume=$(echo "scale=2; 4/3 * $pi * ($radius^3)" | bc)

# Print the volume
echo "The volume of the sphere with radius $radius is $volume"
