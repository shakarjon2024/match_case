kun = int(input("1-7 oralig‘ida son kiriting: "))

match kun:
    case 1:
        print("Dushanba")
    case 2:
        print("Seshanba")
    case 3:
        print("Chorshanba")
    case 4:
        print("Payshanba")
    case 5:
        print("Juma")
    case 6:
        print("Shanba")
    case 7:
        print("Yakshanba")
    case _:
        print("Noto‘g‘ri son!")





ball = int(input("Ballni kiriting: "))

match ball:
    case b if 90 <= b <= 100:
        print("A'lo")
    case b if 75 <= b < 90:
        print("Yaxshi")
    case b if 60 <= b < 75:
        print("Qoniqarli")
    case b if 0 <= b < 60:
        print("Qoniqarsiz")
    case _:
        print("Noto‘g‘ri ball!")





oy = input("Oy nomini kiriting: ").lower()

match oy:
    case "dekabr" | "yanvar" | "fevral":
        print("Qish")
    case "mart" | "aprel" | "may":
        print("Bahor")
    case "iyun" | "iyul" | "avgust":
        print("Yoz")
    case "sentyabr" | "oktyabr" | "noyabr":
        print("Kuz")
    case _:
        print("Bunday oy yo‘q")





buyruq = input("Buyruqni kiriting (left, right, forward, back): ")

match buyruq:
    case "left":
        print("Robot chapga burildi")
    case "right":
        print("Robot o‘ngga burildi")
    case "forward":
        print("Robot oldinga yurdi")
    case "back":
        print("Robot orqaga qaytdi")
    case _:
        print("Noma’lum buyruq")









