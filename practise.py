import json


class SATResultsSystem:
    def __init__(self):
        self.data = []

    def insert_data(self, name, address, city, country, pincode, sat_score):
        passed = "Pass" if sat_score > 30 else "Fail"
        candidate_data = {
            "Name": name,
            "Address": address,
            "City": city,
            "Country": country,
            "Pincode": pincode,
            "SAT Score": sat_score,
            "Passed": passed
        }
        self.data.append(candidate_data)
        print("Data inserted successfully!")

    def view_all_data(self):
        print(json.dumps(self.data, indent=2))

    def get_rank(self, name):
        sorted_data = sorted(self.data, key=lambda x: x["SAT Score"], reverse=True)
        rank = next((i + 1 for i, d in enumerate(sorted_data) if d["Name"] == name), None)
        if rank:
            print(f"{name} has rank #{rank}")
        else:
            print(f"{name} not found in the data.")

    def update_score(self, name, new_score):
        for candidate in self.data:
            if candidate["Name"] == name:
                candidate["SAT Score"] = new_score
                candidate["Passed"] = "Pass" if new_score > 30 else "Fail"
                print(f"{name}'s SAT score updated successfully!")
                return
        print(f"{name} not found in the data.")

    def delete_record(self, name):
        self.data = [candidate for candidate in self.data if candidate["Name"] != name]
        print(f"{name}'s record deleted successfully!")

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            json.dump(self.data, file, indent=2)
        print("Data saved to file successfully!")


def main():
    sat_system = SATResultsSystem()

    while True:
        print("\nMENU:")
        print("1. Insert data")
        print("2. View all data")
        print("3. Get rank")
        print("4. Update score")
        print("5. Delete one record")
        print("6. Save data to file")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            address = input("Enter Address: ")
            city = input("Enter City: ")
            country = input("Enter Country: ")
            pincode = input("Enter Pincode: ")
            sat_score = float(input("Enter SAT Score: "))
            sat_system.insert_data(name, address, city, country, pincode, sat_score)

        elif choice == "2":
            sat_system.view_all_data()

        elif choice == "3":
            name = input("Enter Name to get rank: ")
            sat_system.get_rank(name)

        elif choice == "4":
            name = input("Enter Name to update score: ")
            new_score = float(input("Enter new SAT Score: "))
            sat_system.update_score(name, new_score)

        elif choice == "5":
            name = input("Enter Name to delete record: ")
            sat_system.delete_record(name)

        elif choice == "6":
            filename = input("Enter the filename to save data: ")
            sat_system.save_to_file(filename)

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
