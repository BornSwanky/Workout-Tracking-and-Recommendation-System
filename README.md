
# Workout Tracking and Recommendation System

This repository contains files for a workout tracking and recommendation system, designed to personalize workout routines based on user profiles, fitness goals, and progress. The project includes Python scripts for system functionality and data processing, user and admin interfaces, and a comprehensive report detailing system design and functionality.


## Files

- Report.pdf: A detailed report explaining the system architecture, including a class diagram, personalized workout recommendation strategies, and the design of interactive user and admin interfaces.

- Part_01.py: Python script for defining and managing user profiles, fitness goals, and workout progress. It includes classes and methods for creating user profiles, tracking progress, and generating unique IDs for new users.

- Part_02.py: Python script for generating workout recommendations and interacting with user profiles. It includes the logic for evaluating user performance and updating workout routines based on goals and fitness levels.

- user_profiles.xlsx: Excel file containing mock data of user profiles, including attributes such as age, gender, fitness goals, and workout history.

- workout_fitness_product_sales.xlsx: Excel file containing sales data for workout and fitness-related products, used in the admin interface to visualize sales trends and highlight top users.
## Features 
1. User Profile Management:

Allows users to create fitness profiles with attributes like age, gender, and fitness goals.
Tracks user progress and allows updates to profile data.
Workout Recommendations:

2. Generates personalized workout plans based on user goals and fitness levels.
Provides a list of routines and exercises with varying intensity levels.
Recommends more intense workouts if users seek a greater challenge.
Admin Console:

3. Accessible with a unique login key for system administrators.
Visualizes the sales data of fitness products over the last 10 days.
Highlights the top three users based on fitness performance.

4. Interactive Console
A command-line interface allows users to input and update their fitness information.
Provides a tailored list of workout routines and exercises based on user goals.
Enables system administrators to monitor sales and user activity.
## Documentation

This project has been thoroughly documented in Report.pdf, covering the system's architecture, class design, and logic for personalized workout recommendations. Below is an overview of the main sections documented in the report:

1. Class Diagram and System Structure:

- A class diagram illustrates the main components of the system, focusing on UserProfile and FitnessSystem classes.
- The UserProfile class includes attributes for tracking individual user data, such as user_id, name, age, gender, fitness_goals, current_progress, and next_target.
- The FitnessSystem class manages user profiles, tracking user IDs, and providing functionalities like adding users, listing all users, and updating workout progress.

2. Personalized Workout Recommendations:

- Strategies for generating personalized workout recommendations are described, emphasizing the importance of creating a fitness profile tailored to the user’s goals.
- The system recommends workouts based on user attributes like fitness level, goal (e.g., weight loss, muscle building), and workout intensity.
- The workout history feature records details such as workout type, duration, and intensity to improve recommendation accuracy.

3. Interactive User Interface:

- An interactive, console-based user interface allows new users to create profiles and existing users to update their progress.
- The interface asks users for details like age, gender, fitness goals, and workout history, then recommends tailored workout routines.
- The interface provides a list of about 20 exercise routines that adapt to user preferences and fitness levels.

4. Admin Console:
- The report documents an administrative console accessible with a unique login key (12345) for managing the system.
- Admins can view a sales chart of fitness products over the past 10 days and monitor the top three fitness users based on performance.
- The console supports shutdown functionality, making it easy to end the admin session.

5. Code Snippets and Screenshots:
- The report includes code snippets and screenshots to illustrate key parts of the implementation, providing insights into code structure and logic.
- Example functions include user input validation, personalized recommendation generation, and workout tracking utilities, enhancing user engagement and data accuracy.
For detailed descriptions, code snippets, and images of the system in action, please refer to the Report.pdf file.