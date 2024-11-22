import csv
import random
from tkinter import Tk, Label, Button, Frame, Toplevel


class PatientGenerator:
    def __init__(self, base_path):
        self.base_path = base_path
        self.male_names = self.load_data("male_names.csv")
        self.female_names = self.load_data("female_names.csv")
        self.diseases = self.load_data("diseases.csv")
        self.symptoms1 = self.load_data("symptoms1.csv")
        self.symptoms2 = self.load_data("symptoms2.csv")
        self.body_features = self.load_data("body_features.csv")
        self.institutes = self.load_data("institutes.csv")
        self.generated_patients = []

    def load_data(self, file_name):
        """Load data from a CSV file."""
        try:
            file_path = f"{self.base_path}/{file_name}"
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                return [row[0] for row in reader if row]  # Read only the first column
        except FileNotFoundError:
            print(f"Error: {file_name} not found.")
            return []
        except Exception as e:
            print(f"Error loading {file_name}: {e}")
            return []

    def generate_patient(self):
        """Generate a random patient."""
        gender = random.choice(["Male", "Female"])
        name = random.choice(self.male_names if gender == "Male" else self.female_names)
        age = random.randint(1, 100)
        disease = random.choice(self.diseases)
        symptoms1 = random.choice(self.symptoms1)
        symptoms2 = random.choice(self.symptoms2)
        body_feature = random.choice(self.body_features)
        institute = random.choice(self.institutes)

        patient = {
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Disease": disease,
            "Symptoms": f"{symptoms1}, {symptoms2}",
            "Body Feature": body_feature,
            "Institute": institute
        }

        self.generated_patients.append(patient)
        return patient


# Create a PatientGenerator instance
generator = PatientGenerator(base_path="data")


def display_patient_info():
    """Display a new patient's information."""
    patient = generator.generate_patient()

    # Create a new window for displaying patient info
    info_window = Toplevel()
    info_window.title("Patient Information")

    for key, value in patient.items():
        Label(info_window, text=f"{key}: {value}", font=("Arial", 14)).pack(pady=5)

    Button(info_window, text="Close", command=info_window.destroy).pack(pady=20)


def create_ui():
    """Create the main UI."""
    root = Tk()
    root.title("Patient Generator")
    root.geometry("600x400")
    root.config(bg="#ecf0f1")

    menu_frame = Frame(root, bg="#34495e", width=200)
    menu_frame.pack(side="left", fill="y")

    content_frame = Frame(root, bg="#ecf0f1")
    content_frame.pack(side="right", expand=True, fill="both")

    # Add a title
    Label(content_frame, text="Random Patient Generator", font=("Arial", 18, "bold"), bg="#ecf0f1").pack(pady=20)

    # Add buttons to the menu
    Button(menu_frame, text="Generate Patient", font=("Arial", 12), command=display_patient_info, bg="#16a085", fg="white").pack(pady=10, padx=10, fill="x")

    root.mainloop()


# Run the UI
create_ui()
