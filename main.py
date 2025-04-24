import streamlit as st
import numpy as np

def calculate_clobber(midterm_score, midterm_total, final_score, final_total):
    """Calculate clobbered midterm score based on final performance"""
    final_percentage = final_score / final_total
    clobber_percentage = final_percentage * 0.9  # 90% of final score
    clobber_score = clobber_percentage * midterm_total
    return max(midterm_score, clobber_score)

def get_letter_grade(total_points, a_plus_criteria_met):
    """Determine letter grade based on total points and A+ criteria"""
    if total_points >= 295 and a_plus_criteria_met:
        return 'A+'
    elif total_points >= 285:
        return 'A'
    elif total_points >= 270:
        return 'A-'
    elif total_points >= 255:
        return 'B+'
    elif total_points >= 230:
        return 'B'
    elif total_points >= 210:
        return 'B-'
    elif total_points >= 190:
        return 'C+'
    elif total_points >= 180:
        return 'C'
    elif total_points >= 175:
        return 'C-'
    elif total_points >= 170:
        return 'D+'
    elif total_points >= 165:
        return 'D'
    elif total_points >= 160:
        return 'D-'
    else:
        return 'F'

def main():
    st.title("📘 CS 61A Grade Calculator (Spring 2025)")
    st.write("Easily calculate your grade, including the updated exam clobber policy.")

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.header("Exams")
        mt1 = st.number_input("Midterm 1 (out of 35)", min_value=0.0, max_value=35.0, step=0.5)
        mt2 = st.number_input("Midterm 2 (out of 50)", min_value=0.0, max_value=50.0, step=0.5)
        final = st.number_input("Final Exam (out of 75)", min_value=0.0, max_value=75.0, step=0.5)

    with col2:
        st.header("Other Components")
        projects = st.number_input("Projects (out of 100)", min_value=0.0, max_value=100.0, step=0.5)
        homework = st.number_input("Homework (out of 20)", min_value=0.0, max_value=20.0, step=0.5)
        lab = st.number_input("Lab (out of 10)", min_value=0.0, max_value=10.0, step=0.5)
        discussion = st.number_input("Discussion (out of 10)", min_value=0.0, max_value=10.0, step=0.5)
        extra_credit = st.number_input("Extra Credit (out of 5)", min_value=0.0, max_value=5.0, step=0.5)

    with col3:
        st.header("A+ Criteria")
        st.write("To qualify for A+:")
        st.write("- Score ≥ 295 points")
        st.write("- Correctly answer at least **2 A+ questions**")
        a_plus_questions_correct = st.number_input("A+ Questions Correct", min_value=0, max_value=5, step=1)

    if st.button("Calculate Grade"):
        mt1_clobbered = calculate_clobber(mt1, 35, final, 75)
        mt2_clobbered = calculate_clobber(mt2, 50, final, 75)

        total_points = (mt1_clobbered + mt2_clobbered + final +
                        projects + homework + lab + discussion + extra_credit)

        a_plus_criteria_met = total_points >= 295 and a_plus_questions_correct >= 2

        st.subheader("Results")
        if mt1_clobbered > mt1:
            st.write(f"📈 **Midterm 1 score improved**: {mt1:.1f} → {mt1_clobbered:.1f}")
        if mt2_clobbered > mt2:
            st.write(f"📈 **Midterm 2 score improved**: {mt2:.1f} → {mt2_clobbered:.1f}")

        st.write(f"**Total Points**: {total_points:.1f}/305")
        letter_grade = get_letter_grade(total_points, a_plus_criteria_met)
        st.markdown(f"### **Final Grade**: {letter_grade}")

        if letter_grade == 'A+':
            st.success("🎉 Congratulations! You met the A+ criteria!")
        elif total_points >= 295 and a_plus_questions_correct < 2:
            st.warning("⚠️ You have enough points for A+, but need at least 2 A+ questions correct.")

        st.subheader("Grade Cutoffs Reference")
        cutoffs = """
        - A+ ≥ 295 (with at least 2 A+ questions correct)
        - A  ≥ 285    A- ≥ 270
        - B+ ≥ 255    B  ≥ 230    B- ≥ 210
        - C+ ≥ 190    C  ≥ 180    C- ≥ 175
        - D+ ≥ 170    D  ≥ 165    D- ≥ 160
        """
        st.code(cutoffs)

if __name__ == "__main__":
    main()
