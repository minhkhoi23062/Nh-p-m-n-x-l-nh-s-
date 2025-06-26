import cv2

# Đọc ảnh
img = cv2.imread('fruit.jpg')
clone = img.copy()

# Hàm xử lý click chuột
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Tọa độ: x = {x}, y = {y}")
        # Vẽ chấm đỏ để dễ nhìn
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
        cv2.imshow("Ảnh", img)

# Hiển thị ảnh và bắt sự kiện
cv2.imshow("Ảnh", img)
cv2.setMouseCallback("Ảnh", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
