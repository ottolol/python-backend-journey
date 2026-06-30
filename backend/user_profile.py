user = {
    "name": "Alex",
    "age": 40,
    "city": "Moscow",
    "is_learning_python": True,
    "skills": ["HTML", "CSS", "JAVASCRIPT"],
    "years_of_experience": 2,
    "favorite_technologies": ["React", "Typescript", "Next.JS", "Redux", "RTK query", "Docker", "Git"],
    "computer": {"CPU": "7800x3D", "RAM": 32, "SSD": "980PRO - 1TB", "GPU": "3070ti - 8 gb"},
}

print("=" * 30)
print("USER PROFILE")
print("=" * 30)

print(f"Name: {user['name']}\n")
print(f"Age: {user['age']}\n")
print(f"City: {user['city']}\n")
print(f"Learning Python: {user['is_learning_python']}\n")
print("Skills:")
for skill in user["skills"]:
    print(f" - {skill}")
print(f"\nExperience: {user['years_of_experience']}\n")

print("Favorite technologies:")
for tech in user["favorite_technologies"]:
    print(f" - {tech}")

print("\nComputer:")
for key, value in user["computer"].items():
    print(f" - {key}: {value}")