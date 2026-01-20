

def run_weather_report():
    filename = 'sitka_weather_2018_simple.csv'
    
    # Instruction menu
    print("\n--- Sitka Weather Analysis Tool ---")
    print("Instructions: Enter '1' for Highs, '2' for Lows, or '3' to Exit.")

    while True:
        choice = input("\nMenu: (1) Highs, (2) Lows, or (3) Exit: ").strip()

        if choice == '3':
            print("Thank you for using the Sitka Weather Tool. Goodbye!")
            sys.exit()

        if choice not in ['1', '2']:
            print("Invalid selection. Please enter 1, 2, or 3.")
            continue

        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            dates, temps = [], []
            for row in reader:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                dates.append(current_date)
                
                if choice == '1':
                    # Index 5 is TMAX
                    temp = int(row[5])
                    title = "Daily High Temperatures - 2018"
                    line_color = 'red'
                else:
                    # Index 6 is TMIN
                    temp = int(row[6])
                    title = "Daily Low Temperatures - 2018"
                    line_color = 'blue'
                
                temps.append(temp)

        # Plotting results
        fig, ax = plt.subplots()
        ax.plot(dates, temps, c=line_color)

        # Format plot
        plt.title(title, fontsize=20)
        plt.xlabel('', fontsize=12)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=12)
        plt.tick_params(axis='both', which='major', labelsize=10)

        print(f"Displaying graph for {Sitka Weather}...")
        plt.show()

if __name__ == "__main__":
    run_weather_report()

