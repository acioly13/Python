from tkinter import *
import sys
from datetime import datetime, timedelta
from math import sin, cos, pi
from tkinter import ttk
from astral import LocationInfo
from astral.sun import sun
from timezonefinder import TimezoneFinder
import pytz
import json


class clock:

    ## Constructor.
    #
    # @param len - clock hand lenght.
    # @param wid - clock hand width.
    # @param delta -  time offset for current chosen time
    # @param delta2 -  time offset for second chosen time
    # @param close - used to close the window automatically on tests
    #
    def __init__(self, len=150, wid=None, delta=0, delta2=0, close=0):
        """Constructor"""

        # Clock hand lenght.
        self.len = len

        # Clock hand width.
        self.wid = wid

        # UTC compensation time
        self.delta = delta
        self.delta2 = delta2

        # Location selected for current and second time zone, respectively
        self.chosenLocal = 'None'
        self.chosenLocal2 = 'None'

        # Verify if the window to select the location time zone is open
        self.windowOpen = False

        # Location infos
        self.locationData = self.readLocalTime()

        # Configurations
        MIN_HEIGHT = 600
        MIN_WIDTH = 600

        # Start GMT Watch
        self.timecolor = "red"
        self.sectimecolor = "grey"
        self.root = Tk()
        self.root.title("GMT Watch")
        self.root.geometry('+0+0')
        self.root.minsize(width=MIN_WIDTH, height=MIN_HEIGHT)
        self.root.anchor("center")
        self.canvas = Canvas(self.root, bg="black")
        self.canvas.pack(expand=True, fill="both", anchor="center")
        self.poll()
        self.root.bind("<Button-1>", self.click)
        if close == 0:
            self.root.mainloop()

    ## Converts a vector from polar to Cartesian coordinates.
    # - Note that three hours is in 0º.
    # - However, 0º is twelve hours to the clock.
    #
    # @param angle - vector angle.
    # @param radius - vector lenght .
    # @return 2D point.
    #
    def polar2Cartesian(self, angle, radius=1):
        angle = pi / 2 - angle
        # negative signal means that y increases downwards in the screen
        return (radius * cos(angle), -radius * sin(angle))

    ## Draw a clock hand.
    #
    # @param angle - angle of the clock hand.
    # @param len - lenght of the clock hand.
    # @param wid - width of the clock hand.
    #
    def draw_handle(self, angle, len, wid=None):
        x, y = self.polar2Cartesian(angle, len)
        cx, cy = self.polar2Cartesian(angle, 0.05)
        centerx, centery = self.getScreenCenter()
        # Identify the second time hour
        if wid == 2:
            self.canvas.create_line(cx + centerx, cy + centery, x + centerx, y + centery, fill=self.sectimecolor,
                                    tag='handles', width=wid, capstyle=ROUND)
        else:
            self.canvas.create_line(cx + centerx, cy + centery, x + centerx, y + centery, fill=self.timecolor,
                                    tag='handles', width=wid, capstyle=ROUND)

    ## Draw the clock hands.
    #
    def paint_hms(self):
        # remove just the clock hands
        self.canvas.delete('handles')
        # hora(hour) , minutos(minutes) and segundos(seconds) : UTC time + delta hours (offset)
        # secondHour is the hour of the second time zone selected.
        #
        h, m, s = datetime.timetuple(datetime.utcnow() + timedelta(hours=self.delta))[3:6]
        h2, m2, s2 = datetime.timetuple(datetime.utcnow() + timedelta(hours=self.delta2))[3:6]
        oneMin = pi / 30  # one minute is equal 6 degrees
        fiveMin = pi / 6  # five minutes or one hour is equal 30 degrees
        hora = fiveMin * (h + m / 60.0)
        secondHour = (fiveMin / 2) * (h2 + m2 / 60.0)
        minutos = oneMin * (m + s / 60.0)
        segundos = oneMin * s
        self.draw_handle(minutos, 0.9 * self.len, 10)  # minutes hand for current time zone
        self.draw_handle(hora, 0.5 * self.len, 12)  # hour hand for current time zone
        self.draw_handle(segundos, 0.95 * self.len, 3.6)  # seconds hand for current time zone
        self.draw_handle(secondHour, 1.09 * self.len, 2)  # hour hand for second time zone

    ## Move the clock hands and update all the draw
    # after 200ms.
    #
    def poll(self):
        # self.drawArcs(self.len, self.updateArc_wid())
        self.drawArcs(self.len, 1)
        self.paint_hms()
        self.label12Hours(self.len, self.wid)
        self.label24Hours(self.len, self.wid)
        self.otherStuffDraw(self.len, self.wid)
        self.update_len()
        self.root.after(200, self.poll)

    ## Define the 12-hour marks of the clock
    # @param len - lenght to define the position on the screen.
    # @param wid - draw width.
    #
    def label12Hours(self, len, wid):
        # remove 12-hours marks
        self.canvas.delete('label12')
        for i in range(12):
            angle = (pi / 6) * (i + 1)
            x, y = self.polar2Cartesian(angle, 0.88 * len)
            cx, cy = self.polar2Cartesian(angle, 0.97 * len)
            centerx, centery = self.getScreenCenter()
            self.canvas.create_oval(cx + centerx - 2.5, cy + centery - 2.5, cx + 2.5 + centerx, cy + 2.5 + centery,
                                    fill=self.timecolor, tag='label12', width=wid)
            self.canvas.create_text(x + centerx, y + centery, text=str(i + 1), font="Arial 16", fill=self.timecolor,
                                    tag='label12')

    ## Define the 24-hour marks of the clock
    # @param len - lenght to define the position on the screen.
    # @param wid - draw width.
    #
    def label24Hours(self, len, wid):
        # remove 24-hours marks
        self.canvas.delete('label24')
        for i in range(24):
            angle = (pi / 12) * (i + 1)
            x, y = self.polar2Cartesian(angle, 1.18 * len)
            cx, cy = self.polar2Cartesian(angle, 1.10 * len)
            centerx, centery = self.getScreenCenter()
            self.canvas.create_oval(cx + centerx - 2.5, cy + centery - 2.5, cx + 2.5 + centerx, cy + 2.5 + centery,
                                    fill=self.sectimecolor, tag='label24', width=wid)
            self.canvas.create_text(x + centerx, y + centery, text=str(i + 1), font="Arial 10", fill=self.sectimecolor,
                                    tag='label24')

    ## Draw complementary things of the clock
    # @param len - lenght to define the position on the screen.
    # @param wid - draw width.
    #
    def otherStuffDraw(self, len, wid):
        # remove other Stuff marks
        self.canvas.delete('otherStuff')
        centerx, centery = self.getScreenCenter()
        # Draw the center point of the clock
        self.canvas.create_oval(centerx - 3, centery - 3, centerx + 3, centery + 3, fill="grey", tag='otherStuff',
                                width=wid)
        # Write a text to inform how to change de timezone
        self.canvas.create_text(centerx + len * 1.15, centery + len * 1.35,
                                text="*Left mouse click\nto change timezone", font="Arial 9", fill=self.sectimecolor,
                                tag='otherStuff')
        # Write a text to inform current timezone set
        self.canvas.create_text(centerx - len * 1.05, centery + len * 1.35,
                                text="Current local time: " + self.chosenLocal + "\nSecond local time: " + self.chosenLocal2,
                                font="Arial 9", fill=self.sectimecolor, tag='otherStuff')

    ## Draw arcs to inform day and night times according to the timezone choice.
    # @param len - lenght to define the position on the screen.
    # @param wid - arc width.
    def drawArcs(self, len, wid):
        # remove os arcos
        self.canvas.delete('arc')
        cLen = 1.125
        hr, mr, hs, ms = self.getSunriseSunset(self.chosenLocal, self.locationData)
        hour = pi / 12  # one hour is equal 15 degrees
        hora_r = hour * (hr + mr / 60.0)  # angle of sunrise hour
        hora_s = hour * (hs + ms / 60.0)  # angle of sunset hour
        # start and end angles of the arc
        initialAngle = round(self.radius2degrees(hora_r - pi / 2), 5)  # -pi/2 because arc starts at 6 o'clock
        finalAngle = round(self.radius2degrees(hora_s - pi / 2), 5) - initialAngle
        initialAngle2 = initialAngle + finalAngle
        finalAngle2 = 360 - initialAngle2 + initialAngle
        # rectangle position
        initialPosX = (len * cLen) * cos(pi)
        initialPosY = - (len * cLen) * sin(pi / 2)
        finalPosX = (len * cLen) * cos(0)
        finalPosY = - (len * cLen) * sin(-pi / 2)

        centerx, centery = self.getScreenCenter()

        # Draw day time arc
        # negative angle value is used to compensate the counterclokwise arc angle increase
        self.canvas.create_arc(initialPosX + centerx, initialPosY + centery, finalPosX + centerx, finalPosY + centery,
                               start=-initialAngle, extent=-finalAngle, outline="#FB7F03", tag='arc', width=wid,
                               style=PIESLICE, fill="#FB7F03")
        # Draw night time arc
        self.canvas.create_arc(initialPosX + centerx, initialPosY + centery, finalPosX + centerx, finalPosY + centery,
                               start=-initialAngle2, extent=-finalAngle2, outline="#5C5C5C", tag='arc', width=wid,
                               style=PIESLICE, fill="#5C5C5C")
        # Draw circle around the clock
        self.canvas.create_arc((initialPosX / cLen * 1.30) + centerx - 5, (initialPosY / cLen * 1.30) + centery - 5,
                               (finalPosX / cLen * 1.30) + centerx + 5, (finalPosY / cLen * 1.30) + centery + 5,
                               start=0, extent=359.9, outline="#3C3C3C", tag='arc', width=0.2, style=ARC)
        # Draw the background of the clock
        self.canvas.create_arc((initialPosX / cLen * 0.98) + centerx - 5, (initialPosY / cLen * 0.98) + centery - 5,
                               (finalPosX / cLen * 0.98) + centerx + 5, (finalPosY / cLen * 0.98) + centery + 5,
                               start=0, extent=359.9, outline="#3C3C3C", tag='arc', width=0.2, style=CHORD,
                               fill="black")

    ## Update param len when the window is resized
    #
    #
    def update_len(self):
        self.len = min(self.root.winfo_height(), self.root.winfo_width()) / 3

    ## Get the coordinates of the center of the window
    #  @return 2D point to indicate the center of the GMT Watch window
    #
    def getScreenCenter(self):
        centery = self.root.winfo_height() / 2
        centerx = self.root.winfo_width() / 2
        return (centerx, centery)

    ## Convert radius to degrees
    # @param angle - angle in radius to be converted in degrees
    # @return angle in degrees
    #
    def radius2degrees(self, angle):
        angle = angle * 180 / pi
        return angle

    ## Read a JSON file with the local time informations about some places.
    # Data structure:\n
    # - cities\n
    # - city\n
    # - region\n
    # - offset\n
    # - coordinates\n
    # - latitude\n
    # - longitude
    # @return data - all the information as a dictionary
    #
    def readLocalTime(self):
        try:
            f = open('./localtime.json', 'r')
            # returns JSON object as a dictionary
            data = json.load(f)
            f.close()
        except Exception as e:
            print(e)
            print("No localtime file available ")
        return (data)

    ## Get sunrise e sunset time for a giving time zone
    # @param chosenLocal - City chosen
    # @param locationData - Region information as a dictionary (read from json file)
    # @return hr - sunrise hour
    # @return mr - sunrise minute
    # @return hs - sunset hour
    # @return ms - sunset minute
    #
    def getSunriseSunset(self, chosenLocal, locationData):
        if chosenLocal == "None":
            hr, mr, hs, ms = 6, 0, 18, 0
        else:
            for c in locationData['cities']:
                if c['city'] == chosenLocal:
                    latitude = c['coordinates']['latitude']
                    longitude = c['coordinates']['longitude']
                    region = c['region']
                    local = c['city']
            timezone = (region + "/" + local)
            city = LocationInfo(local, region, timezone, latitude=latitude, longitude=longitude)
            today = datetime.date(datetime.now())
            # Sunrise x sunset
            sun_data = sun(city.observer, today, tzinfo=pytz.timezone(timezone))
            hr, mr, _ = datetime.timetuple(sun_data['sunrise'])[3:6]
            hs, ms, _ = datetime.timetuple(sun_data['sunset'])[3:6]
        return (hr, mr, hs, ms)

    ## Get a mouse click to change the timezone
    # @param e - the position where the mouse was clicked. Not used
    #
    def click(self, e):
        if self.windowOpen is False:
            self.window = Tk()
            self.window.title("Location Time Zone")
            self.window.geometry("300x350")
            self.window.resizable(0, 0)
            self.window.focus_set()
            self.windowOpen = True
            self.window.protocol('WM_DELETE_WINDOW', self.setWindowOpenFalse)
            locals = []
            for c in self.locationData['cities']:
                locals.append(c['city'])
            locals.insert(0, "None")
            lb = Label(self.window, text="\nSelect your current location\n", font=('Arial', 12))
            lb.pack()
            self.cb = ttk.Combobox(self.window, values=locals)
            self.cb.set(self.chosenLocal)
            self.cb.pack()
            lb = Label(self.window, text="\n")
            lb.pack()
            lb = Label(self.window, text="\nSelect a second location\n", font=('Arial', 12))
            lb.pack()
            self.cb2 = ttk.Combobox(self.window, values=locals)
            self.cb2.set(self.chosenLocal2)
            self.cb2.pack()
            lb = Label(self.window, text="\n")
            lb.pack()
            btn = Button(self.window, text="Location selected", font=('Arial', 10), command=self.getLocation)
            btn.pack()
        else:
            self.window.focus_force()

    ## Get chosen location
    #
    def getLocation(self):
        self.chosenLocal = self.cb.get()
        self.chosenLocal2 = self.cb2.get()
        self.window.destroy()
        self.windowOpen = False
        self.changeOffset(self.chosenLocal, self.chosenLocal2, self.locationData)

    ## Change the timezone of GMT Watch
    # @param chosenLocal - Current city chosen for local time
    # @param chosenLocal2 - Second city chosen for second local time
    # @param locationData - Region information as a dictionary (read from json file)
    #
    def changeOffset(self, chosenLocal, chosenLocal2, locationData):
        for c in locationData['cities']:
            if chosenLocal == 'None':
                delta = 0
            elif chosenLocal == c['city']:
                timezone = c['region'] + "/" + c['city']
                delta = pytz.timezone(timezone).utcoffset(datetime.now()).total_seconds() / 3600
            if chosenLocal2 == 'None':
                delta2 = 0
            elif chosenLocal2 == c['city']:
                timezone = c['region'] + "/" + c['city']
                delta2 = pytz.timezone(timezone).utcoffset(datetime.now()).total_seconds() / 3600
        self.delta = delta
        self.delta2 = delta2

    ## Set var windowOpen to false when the local select window is closed using X button
    #
    def setWindowOpenFalse(self):
        self.window.destroy()
        self.windowOpen = False


## Main
def main():
    clock()


if __name__ == "__main__":
    sys.exit(main())
