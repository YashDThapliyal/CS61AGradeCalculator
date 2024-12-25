import streamlit as st
import numpy as np

def calculate_clobber(midterm_score, midterm_total, final_score, final_total):
    """Calculate clobbered midterm score based on final performance"""
    final_percentage = final_score / final_total
    clobber_percentage = final_percentage * 0.9  # 90% of final score
    clobber_score = clobber_percentage * midterm_total
    return max(midterm_score, clobber_score)

def get_letter_grade(total_points):
    """Determine letter grade based on total points"""
    if total_points >= 285:
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
    st.title("CS 61A Grade Calculator")
    st.write("Calculate your CS 61A grade including exam clobber policy")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Exams")
        mt1 = st.number_input("Midterm 1 (out of 40)", min_value=0.0, max_value=40.0, step=0.5)
        mt2 = st.number_input("Midterm 2 (out of 45)", min_value=0.0, max_value=45.0, step=0.5)
        final = st.number_input("Final Exam (out of 75)", min_value=0.0, max_value=75.0, step=0.5)
    
    with col2:
        st.subheader("Other Components")
        projects = st.number_input("Projects (out of 100)", min_value=0.0, max_value=100.0, step=0.5)
        homework = st.number_input("Homework (out of 20)", min_value=0.0, max_value=20.0, step=0.5)
        lab = st.number_input("Lab (out of 10)", min_value=0.0, max_value=10.0, step=0.5)
        discussion = st.number_input("Discussion (out of 10)", min_value=0.0, max_value=10.0, step=0.5)
        extra_credit = st.number_input("Extra Credit (out of 4)", min_value=0.0, max_value=4.0, step=0.5)

    if st.button("Calculate Grade"):
        mt1_clobbered = calculate_clobber(mt1, 40, final, 75)
        mt2_clobbered = calculate_clobber(mt2, 45, final, 75)
        
        total_points = (mt1_clobbered + mt2_clobbered + final + 
                       projects + homework + lab + discussion + extra_credit)
        
        st.subheader("Results")
        
        if mt1_clobbered > mt1:
            st.write(f"📈 Midterm 1 score improved from {mt1:.1f} to {mt1_clobbered:.1f} due to clobber")
        if mt2_clobbered > mt2:
            st.write(f"📈 Midterm 2 score improved from {mt2:.1f} to {mt2_clobbered:.1f} due to clobber")
        
        st.write(f"Total Points: {total_points:.1f}/304")
        letter_grade = get_letter_grade(total_points)
        st.markdown(f"### Final Grade: {letter_grade}")
           
        st.subheader("Grade Cutoffs Reference")
        cutoffs = """
        A  ≥ 285    A- ≥ 270
        B+ ≥ 255    B  ≥ 230    B- ≥ 210
        C+ ≥ 190    C  ≥ 180    C- ≥ 175
        D+ ≥ 170    D  ≥ 165    D- ≥ 160
        """
        st.code(cutoffs)

if __name__ == "__main__":
    main()
