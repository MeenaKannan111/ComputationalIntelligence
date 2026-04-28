def get_prob(prompt):
    """Helper to ensure input is a valid probability float."""
    while True:
        try:
            val = float(input(prompt))
            if 0 <= val <= 1:
                return val
            print("Enter a probability between 0 and 1!")
        except ValueError:
            print("Invalid input! Please enter a number.")

# Step 1: Compute Joint Probabilities from User Input
def compute_joint():
    print("\nEnter Joint Probabilities P(Study, Pass):")
    print("(Note: Ideally, these four should sum to 1.0)")
    
    joint = {}
    # (Study, Pass) -> 1 is True, 0 is False
    # P(S and P)
    joint[(1, 1)] = get_prob("P(Study=True, Pass=True): ")
    # P(S and not P)
    joint[(1, 0)] = get_prob("P(Study=True, Pass=False): ")
    # P(not S and P)
    joint[(0, 1)] = get_prob("P(Study=False, Pass=True): ")
    # P(not S and not P)
    joint[(0, 0)] = get_prob("P(Study=False, Pass=False): ")

    total = sum(joint.values())
    if abs(total - 1.0) > 0.01:
        print(f"\n[Warning] Your inputs sum to {total:.2f}. Normalizing to 1.0...")
        for key in joint:
            joint[key] /= total

    print("\n--- Joint Probability Table ---")
    print(f"P(Study & Pass)    = {joint[(1,1)]:.4f}")
    print(f"P(Study & Fail)    = {joint[(1,0)]:.4f}")
    print(f"P(No Study & Pass) = {joint[(0,1)]:.4f}")
    print(f"P(No Study & Fail) = {joint[(0,0)]:.4f}")
    return joint

# Step 2: Simple (Marginal) Probability
def simple_prob(joint):
    print("\n--- Simple (Marginal) Probabilities ---")
    # P(Study) = P(Study & Pass) + P(Study & Fail)
    p_study = joint[(1, 1)] + joint[(1, 0)]
    # P(Pass) = P(Study & Pass) + P(No Study & Pass)
    p_pass = joint[(1, 1)] + joint[(0, 1)]

    print(f"P(Student Studied) = {p_study:.4f}")
    print(f"P(Student Passed)  = {p_pass:.4f}")
    return p_study, p_pass

# Step 3: Joint Inference (AND / OR)
def joint_inference(joint, p_study, p_pass):
    print("\n--- Joint Probability Inference ---")
    p_and = joint[(1, 1)]
    p_or = p_study + p_pass - p_and
    
    print(f"P(Studied AND Passed) = {p_and:.4f}")
    print(f"P(Studied OR Passed)  = {p_or:.4f}")
    return p_and

# Step 4: Bayes / Conditional Probability
def bayes_inference(joint, p_study, p_pass):
    print("\n--- Conditional (Bayes) Probability ---")
    # P(Pass | Study) = P(Pass and Study) / P(Study)
    p_pass_given_study = joint[(1, 1)] / p_study if p_study > 0 else 0
    # P(Study | Pass) = P(Study and Pass) / P(Pass)
    p_study_given_pass = joint[(1, 1)] / p_pass if p_pass > 0 else 0
    
    print(f"P(Pass | Study) = {p_pass_given_study:.4f}")
    print(f"P(Study | Pass) = {p_study_given_pass:.4f}")

def main():
    joint = compute_joint()
    while True:
        print("\n====== MENU ======")
        print("1. Simple Probability")
        print("2. Joint Inference")
        print("3. Bayes/Conditional Probability")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            simple_prob(joint)
        elif choice == '2':
            ps, pp = simple_prob(joint)
            joint_inference(joint, ps, pp)
        elif choice == '3':
            ps, pp = simple_prob(joint)
            bayes_inference(joint, ps, pp)
        elif choice in ('4', 'exit'):
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
