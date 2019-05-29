
from datetime import date
import matplotlib.dates
from pylab import *
from numpy import array,sin,pi

def createBiorythm(dob, target):
    t0 = dob.toordinal()
    t1= target.toordinal()
    t = array(range((t1-30), (t1+30))) # range 30 days before and after the target date
    bio = 100*[sin(2*pi*(t-t0)/23),  # Physical
         sin(2*pi*(t-t0)/28),  # Emotional
         sin(2*pi*(t-t0)/33)]; # Intellectual
    t1 = target.toordinal()
    label = []
    for p in t:
        print(date.fromordinal(p))
        label.append(date.fromordinal(p))
    fig = figure()
    ax = fig.gca()
    plot(label, bio[0], label, bio[1], label, bio[2])
    legend(['Physical', 'Emotional', 'Intellectual']) # adding legend
    ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%b/%d'))
    show()

year = int(input('Enter birth year: '))
month = int(input('Enter birth month: '))
day = int(input('Enter birth day: '))
date1 = datetime.date(year, month, day)
year = int(input('Enter target year: '))
month = int(input('Enter target month: '))
day = int(input('Enter target day: '))
date2 = datetime.date(year, month, day)
createBiorythm(date1, date2);
