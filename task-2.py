time_in_seconds = int(input("Enter time in seconds: "));

hours = time_in_seconds // 3600;
time_left = time_in_seconds % 3600;

minutes = time_left // 60;
seconds = time_left % 60;

print(f"{hours:02d}:{minutes:02d}:{seconds:02d}");
