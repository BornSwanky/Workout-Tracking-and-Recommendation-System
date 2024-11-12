import pandas as pd
import matplotlib.pyplot as plt

class WorkoutProduct:
    def __init__(self, product_id, name, category, sales):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.sales = sales

class User:
    def __init__(self, user_id, name, age, gender, fitness_goal, fitness_level, score):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.gender = gender
        self.fitness_goal = fitness_goal
        self.fitness_level = fitness_level
        self.score = score

class AdminConsole:
    def __init__(self, workout_fitness_product_sales_df, user_profiles_df):
        self.workout_products = []
        self.users = []
        self.login_key = "12345"
        self.workout_fitness_product_sales = workout_fitness_product_sales_df
        self.user_profiles_df = user_profiles_df

    def authenticate(self):
        entered_key = input("Enter the login key: ")
        return entered_key == self.login_key

    def generate_sample_data(self, users_df, products_df):
        # Load products data
        for index, row in products_df.iterrows():
            date = row['Date']
            for category, sales in row.items():
                if category != 'Date':
                    product_id = f"{date}-{category}"
                    name = f"{category} {date}"
                    self.workout_products.append(WorkoutProduct(product_id, name, category, sales))

        # Load users data
        for index, row in users_df.iterrows():
            user = User(row['User ID'], row['Name'], row['Age'], row['Gender'], 
                        row['Fitness Goal'], row['Fitness Level'], row['Score'])
            self.users.append(user)

    def display_sales_chart(self):
        # Ensure the 'Date' column is treated as a string
        self.workout_fitness_product_sales['Date'] = self.workout_fitness_product_sales['Date'].astype(str)

        # Extracting the necessary data
        dates = self.workout_fitness_product_sales['Date']
        workout_sales = self.workout_fitness_product_sales['Workout Products Sales ']
        fitness_sales = self.workout_fitness_product_sales['Fitness Products Sales ($)']

        # Creating a bar chart
        plt.figure(figsize=(12, 8))
        plt.barh(dates, workout_sales, color='blue', label='Workout Product Sales')
        plt.barh(dates, fitness_sales, color='green', left=workout_sales, label='Fitness Product Sales')
        plt.xlabel('Sales ($)')
        plt.ylabel('Date')
        plt.title('Sales of Workout and Fitness Products Over the Last 10 Days')
        plt.legend()
        plt.tight_layout()
        plt.show()

    def display_top_users(self):
        # Sorting the users based on their scores
        sorted_users = self.user_profiles_df.sort_values(by='Score', ascending=False)[:3]

        # Data for plotting
        user_names = sorted_users['Name']
        user_scores = sorted_users['Score']

        # Creating a bar chart for the top users
        plt.figure(figsize=(8, 6))
        plt.bar(user_names, user_scores, color='green')
        plt.xlabel('Name')
        plt.ylabel('Score')
        plt.title('Top 3 Users Based on Score')
        plt.tight_layout()
        plt.show()

    def run(self):
        if not self.authenticate():
            print("Authentication failed. Access denied.")
            return

        while True:
            self.display_admin_menu()
            option = input("Please choose 1-3: ")

            if option == "1":
                self.display_sales_chart()
            elif option == "2":
                self.display_top_users()
            elif option == "3":
                self.shutdown_system()
                break
            else:
                print("Option unavailable, please try 1-3 again.")

    def display_admin_menu(self):
        print("Admin Console Menu")
        print("1. Display Workout and Fitness Product Sales Chart")
        print("2. Display Top Users by Score")
        print("3. Gracefully Shut Down the System / Exit")

    def shutdown_system(self):
        print("Shutting down the system for maintenance or updates...")

def main():
    # Load CSV data
    user_profiles_df = pd.read_csv(r'D:\Downloads\user_profiles.csv')
    workout_fitness_product_sales_df = pd.read_csv(r'D:\Downloads\workout_fitness_product_sales.csv')

    # Creating an instance of the AdminConsole with the loaded data
    admin_console = AdminConsole(workout_fitness_product_sales_df, user_profiles_df)
    admin_console.generate_sample_data(user_profiles_df, workout_fitness_product_sales_df)

    # Run the console
    admin_console.run()

if __name__ == "__main__":
    main()
