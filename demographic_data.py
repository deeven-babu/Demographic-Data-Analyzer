
import pandas as pd

def  calculate_demographic_data(print_data = True):
    # Load dataset
    df = pd.read_csv("adult_data.csv")


    # 1. How many people of each race?
    race_count = df["race"].value_counts()



    # 2. What is the average age of men?
    avg_men_age = round(
        df[df["sex"] == "Male"]["age"].mean(), 1
    )


    # 3. What percentage of people have a Bachelor's degree?
    bachelor_deg = round(
        (df["education"] == "Bachelors").mean() * 100, 1
    )


    # 4. What percentage of people with advanced education
    # make more than 50K?
    higher_edu = df[
        df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    ]

    high_edu_sal = round(
        (higher_edu["salary"] == ">50K").mean() * 100, 1
    )


    # 5. What percentage of people without advanced education
    # make more than 50K?
    nrml_edu = df[
        ~df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    ]

    nrml_edu_sal = round(
        (nrml_edu["salary"] == ">50K").mean() * 100, 1
    )


    # 6. What is the minimum number of hours worked per week?
    min_work_hours = df["hours-per-week"].min()


    # 7. What percentage of people working minimum hours
    # earn more than 50K?
    num_min_workers = df[
        df["hours-per-week"] == min_work_hours
    ]

    min_nof_hrs_earn_50K = round(
        (num_min_workers["salary"] == ">50K").mean() * 100, 1
    )


    # 8. Which country has the highest percentage of people
    # earning more than 50K?
    country_count = df["native-country"].value_counts()

    country_rich = df[
        df["salary"] == ">50K"
    ]["native-country"].value_counts()

    country_percentage = (country_rich / country_count) * 100

    highest_earning_country = country_percentage.idxmax()

    highest_earning_country_percentage = round(
        country_percentage.max(), 1
    )



    # 9. What is the most popular occupation for people
    # earning more than 50K in India?
    top_IN_occupation = df[
        (df["native-country"] == "India") &
        (df["salary"] == ">50K")
    ]["occupation"].value_counts().idxmax()

    print("Most popular occupation in India:", top_IN_occupation)


    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", avg_men_age)
        print("Percentage with Bachelor's degree:", bachelor_deg)
        print("Percentage with higher education earning >50K:", high_edu_sal)
        print("Percentage without higher education earning >50K:", nrml_edu_sal)
        print("Minimum work hours:", min_work_hours)
        print("Percentage of minimum-hours workers earning >50K:", min_nof_hrs_earn_50K)
        print("Country with highest percentage earning >50K:", highest_earning_country)
        print("Percentage of people earning >50K in that country:", highest_earning_country_percentage)
        print("Most popular occupation in India:", top_IN_occupation)

        # Return results
    return {
        "race_count": race_count,
        "average_age_men": avg_men_age,
        "percentage_bachelors": bachelor_deg,
        "higher_education_rich": high_edu_sal,
        "lower_education_rich": nrml_edu_sal,
        "min_work_hours": min_work_hours,
        "rich_percentage": min_nof_hrs_earn_50K,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }