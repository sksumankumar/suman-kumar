import cv2
import matplotlib.pyplot as plt
        
# Hide grid lines
fig, ax = plt.subplots(figsize=(10,10))
ax.grid(False)
    
im=cv2.imread("C:\\Users\\91895\\Downloads\\dog.jpg")
plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
plt.show()

