#import matplotlib.pyplot as plt
#import numpy as np
#
#y = np.array([35, 25, 25, 15])
#
#plt.pie(y)
#plt.show() 

#import matplotlib.pyplot as plt
#import numpy as np
#
#y = np.array([35, 25, 25, 15])
#mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
#
#plt.pie(y, labels = mylabels)
#plt.show() 

#import matplotlib.pyplot as plt
#import numpy as np
#
#y = np.array([35, 25, 25, 15])
#mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
#
#plt.pie(y, labels = mylabels, startangle = 90)
#plt.show() 


#import matplotlib.pyplot as plt
#import numpy as np
#
#y = np.array([35, 25, 25, 15])
#mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
#
#plt.pie(y, labels = mylabels)
#plt.legend()
#plt.show() 

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show() 
