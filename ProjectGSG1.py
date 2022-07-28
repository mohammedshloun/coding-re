import csv
class Passenger():
    def __init__(self):
        self.passenger_name = None
        self.passenger_number = None
        self.departure_location = None
        self.destination_location = None
        self.ddmmyyyy = None
        self.seat_number = None
        self.THE_Bus_Type = None
        self.bus_fare = None
        self.cars_company = 1
        self.countcol = 0

    def get_Passenger_Info(self):
        self.passenger_name = input("Enter Passenger Name :")
        self.passenger_number = int(input("Enter Number Of Passenger :"))

        print("2: Gaza")

        self.d_l = int(input("Enter Departure Location"))
        if self.d_l == 1:
            self.departure_location = "Gaza"
        else:
            print("Please Enter The correct choice  :")
        # departure Location Name END
        print("1: Jerusalem")
        print("2: Ramallah")
        print("3: Jenin")
        print("4: Nablus")
        print("5: Akko")

        self.d_p_l = int(input("Enter Destination Location  :"))
        if self.d_p_l == 1:
            self.destination_location = "Jerusalem"
        elif self.d_p_l == 2:
            self.destination_location = "Ramallah"
        elif self.d_p_l == 3:
            self.destination_location = "Jenin"
        elif self.d_p_l == 4:
            self.destination_location = "Nablus"
        elif self.d_p_l == 5:
            self.destination_location = "Akko"
        else:
            print("Please Enter The correct choice  :")


        self.ddmmyyyy = input("Enter The Date of Journey Like 25/07/2022 :")


        print("[1]__[2]__[3]__[4]__[5]__[6]__[7]__[8]__[9]__[10]")
        print("[11]_[12]_[13]_[14]_[15]_[16]_[17]_[18]_[19]_[20]")
        print("[21]_[22]_[23]_[24]_[25]_[26]_[27]_[28]_[29]_[30]")

        seat_no_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                      28, 29, 30]
        self.booking_list = []
        while True:
            self.seat_no = int(input("Choose a Seat Number & Max To Max You Can Book Two Ticket  :"))
            if self.seat_no <= 30:

                if self.seat_no in seat_no_list:
                    self.booking_list.append(self.seat_number)
                    del seat_no_list[self.seat_number + 1]
                    count = len(seat_no_list)
                else:
                    print("Ticket Allready Booked")
                print("Do You Want To Book One More Seat Enter (Yes/No)")
                y = input("")
                if y == "Yes":
                    pass
                else:
                    break

            else:
                print("Don't Choose a Seat Number Which is Not Available")
                # Booking Seat END

        print(" 1. AC BUS     = 500 Fare")
        print(" 2. NON AC BUS = 300 Fare")
        self.THE_Bus_Type = int(input("Select Bus Type  :"))

        if self.THE_Bus_Type == 1:
            self.select_Bus_Type = "AC BUS"
            self.bus_fare = self.passenger_number * 500
        elif self.THE_Bus_Type == 2:
            self.select_Bus_Type = "NON AC BUS"
            self.bus_fare = self.passenger_number * 300


class Passenger_Data_Csv(Passenger):
    def save_info(self):
        try:
            with open("passenger_Data.csv", 'r+', newline="") as f:
                r = csv.reader(f)
                data = list(r)

                for i in data:
                    self.cars_company += 1
                    for j in i:
                        self.countcol += 1
                    print()
                print("Number of Records Are Found In Database :", self.cars_company)

        except:
            print("File has not available")
        finally:
            with open("passenger_Data.csv", 'a+', newline="") as f:
                w = csv.writer(f)
                w.writerow([self.cars_company, self.passenger_name, self.passenger_number, self.departure_location,
                            self.destination_location, self.ddmmyyyy, self.booking_list, self.THE_Bus_Type,
                            self.bus_fare])
                print("Data Save successfully")
                print()


'''pd_obj = Passenger_Data_Csv()
pd_obj.get_Passenger_Info()
pd_obj.save_info()'''
