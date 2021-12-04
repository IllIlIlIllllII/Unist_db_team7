-- UserID는 1로 주시면 될 것 같습니다.

---------------------------------- 1. region에 따른 list up ----------------------------------
-- input : ProductRegion - "Jeju" or "Soeul" or "Ulsan"
SELECT * FROM Product WHERE ProductRegion=%s;


---------------------------------- 2-1. 가격순 list up ----------------------------------
-- input : 없음.
SELECT * FROM Product ORDER BY ProductPrice ASC;

---------------------------------- 2-2. 특정 여행사 list up ----------------------------------
-- input : ProductCompany - "Samsung" or "Apple"
SELECT * FROM Product WHERE ProductCompany="APPLE";

---------------------------------- 3. 장바구니 list up ----------------------------------
-- input : UserID
SELECT * FROM Cart JOIN Product ON Cart.ProductID = Cart.ProductID WHERE Cart.UserID=%s;

---------------------------------- 4. 장바구니 넣기 ----------------------------------
-- 수량 없이 하겠습니다.
-- input : ProductID, UserID, ProductName, ProductPrice
INSERT INTO Cart (ProductId, UserId, ProductName, Amount, ProductPrice)
		VALUES (%s, %s, %s, 1, %s);

---------------------------------- 5-1. 쿠폰 list 가져오기 ----------------------------------
-- input : UserID
SELECT * FROM Coupon WHERE UserID=%s AND UsedCheck=FALSE;

---------------------------------- 5-2. 쿠폰 적용하기 ----------------------------------
-- input : ProductID, CouponID, UserID
-- output : NewPrice, DiscountedPrice
SELECT Product.ProductPrice - Coupon.DiscountAmount as NewPrice,
       Coupon.DiscountAmount as DiscountedPrice
        FROM Product JOIN Coupon 
        WHERE Product.ProductID=%s AND
              Coupon.CouponID=%s AND Coupon.UserID=%s;

---------------------------------- 6. 구매하기 ----------------------------------
-- input : ProductID, UserID, TotalPrice, CouponID(optional)
-- coupon 미사용시 CouponID = 0
INSERT INTO Purchase (ProductID, UserID, TotalPrice, CouponID)
    VALUES (%s, %s, %s, %s);

-- 쿠폰 사용시 아래 쿼리도 실행
-- input : ProductID, UserID
UPDATE Coupon SET UsedCheck=TRUE WHERE ProductID=%s AND UserID=%s;








