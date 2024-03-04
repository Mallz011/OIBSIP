from io import BytesIO
import tkinter as tk
import requests
from PIL import Image, ImageTk
from tkinter import messagebox

#implement class WeatherApplication
class WeatherApplication():
    #method to implement weather app interface
    def __init__(self, master):
        self.master = master
        self.master.title("Weather Application")

        self.locationLabel = tk.Label(master, text = "Enter city name: ")
        self.locationLabel.pack()

        self.locationEntry = tk.Entry(master)
        self.locationEntry.pack()

        self.searchButton = tk.Button(master, text = "Search", command = self.searchWeather)
        self.searchButton.pack()

        self.weatherFrame = tk.Frame(master)
        self.weatherFrame.pack()

        self.weatherLabel = tk.Label(self.weatherFrame, text = "")
        self.weatherLabel.pack()

        self.weatherIconLabel = tk.Label(self.weatherFrame)
        self.weatherIconLabel.pack()

        self.units = tk.StringVar()
        self.units.set("metric")

        self.unitRadioFrame = tk.Frame(master)
        self.unitRadioFrame.pack()

        self.metricRadio = tk.Radiobutton(self.unitRadioFrame, text = "Metric", variable = self.units, value = "metric")
        self.metricRadio.pack()

        self.imperialRadio = tk.Radiobutton(self.unitRadioFrame, text= "Imperial", variable = self.units, value = "imperial")
        self.imperialRadio.pack()
    #method used to implement weather search
    def searchWeather(self):
        rq = requests
        city = self.locationEntry.get()
        units = self.units.get()
        apiKey = '9e2b1cd1be621688034a20f11a64471d' #api key used for weather service
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units={units}"

        try:
            response = rq.get(url)
            data = response.json()

            if data["cod"] == 200:
                weatherDescription = data["weather"][0]["description"]
                temperature = data["main"]["temp"]
                iconId = data["weather"][0]["icon"]
                iconUrl = f"http://openweathermap.org/img/wn/{iconId}.png" 

                self.weatherLabel.config(text = f"Description: {weatherDescription}\n Temperature: {temperature}")

                iconImage = self.getWeatherIcon(iconUrl) #implement method to get icon
                self.weatherIconLabel.config(image = iconImage)
                self.weatherIconLabel.image = iconImage
            else:
                messagebox.showerror("Error", "Unable to find City")
        except Exception as e:
            messagebox.showerror("Error", f"An error occured: {str(e)}")
    #method to get weather icon when printing results
    def getWeatherIcon(self, url):
        rq = requests
        response = rq.get(url)
        iconData = response.content
        iconImage = Image.open(BytesIO(iconData))
        iconPhoto = ImageTk.PhotoImage(iconImage)
        return iconPhoto, iconImage

def main():
    root = tk.Tk()
    app = WeatherApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()