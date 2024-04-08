n = int(input())
genres = {}

for _ in range(n):
    info = input().split()

    if len(info) == 3:
        age, gender, genre = info
        age = int(age)

        if gender not in genres:
            genres[gender] = {}

        if genre not in genres[gender]:
            genres[gender][genre] = [float('inf'), 0]

        genres[gender][genre][0] = min(age, genres[gender][genre][0])
        genres[gender][genre][1] = max(age, genres[gender][genre][1])
    else:
        age, gender = info
        age = int(age)

        found_genre = False

        if gender in genres:
            for known_genre, (min_age, max_age) in genres[gender].items():
                if min_age <= age <= max_age:
                    print(known_genre)
                    found_genre = True
                    break

        if not found_genre:
            print("None")
