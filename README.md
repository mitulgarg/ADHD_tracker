# ADHD_tracker

This is a program made for students with Attention Deficit Hyperactivity Disorder or ADHD
The OpenCV module accesses the front camera and detects excessive physical movement, thus showing lack of sitting and paying attention while doing a particular task.
The timestamps of movement are recorded and updated in an excel database 'Time_of_movements.csv' .
This data is finally plotted and used for knowledge purposes, to know when and at which points and how often 
was the ADHD student paying attention while doing his work and not moving around.
The future of this project includes, giving good promptds to the student to breathe, calm down and focus.
This is also used as a doctors dataset, and medication and knowledge of movement can therefore be plotted and analyzed.


## Getting Started

To run the motion detector, follow these steps:

1. Install the required libraries:

   ```bash
   pip install numpy matplotlib opencv-python pandas
   ```

2. Run the `motion_detector.py` script:

   ```bash
   python motion_detector.py
   ```

3. Press 'q' to exit the program.

## Dependencies

- [NumPy](https://numpy.org/): For numerical operations.
- [Matplotlib](https://matplotlib.org/): For plotting graphs.
- [OpenCV](https://opencv.org/): For computer vision tasks.
- [Pandas](https://pandas.pydata.org/): For handling time-related operations.

## Usage

- The program will display a GUI window encouraging the user to focus. Click "Continue" to proceed.
- The webcam will start capturing frames, and the motion detector will draw green rectangles around moving objects.
- Motion events are recorded with start and end times in a CSV file named "Time_ofmovements.csv."
- The program generates a scatter plot showing the time of movements.

## Additional Notes

- The program uses Tkinter for a simple GUI. Note that Tkinter may not work well on some platforms or environments.
- Make sure your webcam is connected and accessible by the program.
- The program allows you to exit by pressing 'q.'


## Acknowledgments

- The motion detector code is inspired by computer vision concepts and OpenCV functionalities.
