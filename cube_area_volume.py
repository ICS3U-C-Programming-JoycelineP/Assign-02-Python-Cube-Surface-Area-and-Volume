#!/usr/bin/env python3
# created by: Joyceline
# created on: Oct 10 2026
# This Program calculates the surface area and volume of a cube.
import math


def main():
    # get the edge length of the cube from the user and convert to float
    edge_length = float(input("Enter the edge length of the cube (cm): "))

    # calculate the surface area and volume of the cube
    surface_area = 6 * (edge_length * edge_length)
    volume = edge_length * edge_length * edge_length

    # Display the surface area and volume to the user with proper units
    print("")
    print("Surface Area is {:.2f} cm².".format(surface_area))
    print("Volume is {:.2f} cm³.".format(volume))


if __name__ == "__main__":
    main()
