import streamlit as st

# Function to display interesting facts
def display_interesting_facts(years_remaining):
    if years_remaining <= 1:
        return "Make the most of your time! Every moment counts."
    elif years_remaining <= 5:
        return "Time flies! Make sure you continue to cherish every day."
    elif years_remaining <= 10:
        return "You still have plenty of time ahead. Keep pursuing your dreams!"
    else:
        return "Life is full of possibilities. Enjoy the journey!"

# Streamlit app
def main():
    st.title("Life Expectancy Calculator")
    st.markdown("Calculate how much time you have left to live and discover interesting facts about it!")

    age = st.number_input("What is your current age?", min_value=0, step=1)
    desired_age = st.number_input("To what age do you wish to live?", min_value=age, step=1)

    years_remaining = desired_age - age
    days_remaining = years_remaining * 365
    weeks_remaining = years_remaining * 52
    months_remaining = years_remaining * 12
    hours_remaining = years_remaining * 365 * 24

    st.success(
        f"You have **{days_remaining:,}** days, **{weeks_remaining:,}** weeks, **{months_remaining:,}** months, and **{hours_remaining:,}** hours remaining to live on this earth if you are really going to live for **{desired_age}** years"
    )

    if years_remaining < 0:
        st.warning("Congratulations! You have already exceeded your desired age.")
    else:
        st.write("")
        st.info("Interesting Facts About Your Remaining Time:")
        fact = display_interesting_facts(years_remaining)
        st.write(f"🌟 {fact}")

    st.write("")
    st.markdown("### 🚀 How to Make the Most of Your Remaining Time")
    st.write("Life is a precious gift, and every moment counts. Here are some tips to help you make the most of your remaining time:")

    st.write("1. **Set Meaningful Goals:** Identify what you want to achieve and work towards it.")
    st.write("2. **Cherish Relationships:** Spend quality time with your loved ones and create lasting memories.")
    st.write("3. **Embrace New Experiences:** Step out of your comfort zone and try new things.")
    st.write("4. **Stay Healthy:** Take care of your physical and mental well-being.")
    st.write("5. **Practice Gratitude:** Focus on the positive aspects of life and be grateful for every day.")
    st.write("6. **Spread Kindness:** Make a positive impact on others through acts of kindness.")
    st.write("7. **Learn and Grow:** Keep learning, growing, and evolving as a person.")

    st.write("")
    st.markdown("### 🌍 Life is an Adventure")
    st.write("Remember, life is an incredible adventure full of opportunities and challenges. Embrace each moment and create a life that you're proud of!")

if __name__ == "__main__":
    main()
