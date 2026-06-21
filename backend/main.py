from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal,engine
import models
import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message":"Student Marketplace API"}

@app.post("/register")
def register(user: schemas.UserCreate,
             db: Session = Depends(get_db)):

    existing_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = models.User(
        full_name=user.full_name,
        email=user.email,
        password=user.password,
        phone=user.phone,
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message":"User Registered Successfully"}

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message":"User Registered"}

@app.post("/login")
def login(user:schemas.LoginSchema,db:Session=Depends(get_db)):

    existing = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if not existing:
        raise HTTPException(
            status_code=404,
            detail="User Not Found"
        )

    if existing.password != user.password:
        raise HTTPException(
            status_code=401,
            detail="Wrong Password"
        )

    return {"message":"Login Successful"}

@app.get("/users")
def users(db:Session=Depends(get_db)):
    return db.query(models.User).all()

@app.get("/profile/{user_id}")
def profile(user_id:int,db:Session=Depends(get_db)):
    return db.query(models.User).filter(
        models.User.id == user_id
    ).first()

@app.put("/profile/{user_id}")
def update_profile(
    user_id:int,
    user:schemas.UserCreate,
    db:Session=Depends(get_db)
):
    existing = db.query(models.User).filter(
        models.User.id == user_id
    ).first()

    existing.full_name = user.full_name
    existing.email = user.email
    existing.password = user.password
    existing.phone = user.phone
    existing.role = user.role

    db.commit()

    return {"message":"Profile Updated"}

@app.post("/products")
def add_product(
    product:schemas.ProductCreate,
    db:Session=Depends(get_db)
):
    new_product = models.Product(
        title=product.title,
        description=product.description,
        category=product.category,
        price=product.price,
        seller_name=product.seller_name
    )

    db.add(new_product)
    db.commit()

    return {"message":"Product Added"}

@app.get("/products")
def all_products(db:Session=Depends(get_db)):
    return db.query(models.Product).all()

@app.get("/products/{product_id}")
def single_product(
    product_id:int,
    db:Session=Depends(get_db)
):
    return db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()

@app.put("/products/{product_id}")
def update_product(
    product_id:int,
    product:schemas.ProductCreate,
    db:Session=Depends(get_db)
):
    existing = db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()

    existing.title = product.title
    existing.description = product.description
    existing.category = product.category
    existing.price = product.price
    existing.seller_name = product.seller_name

    db.commit()

    return {"message":"Product Updated"}

@app.delete("/products/{product_id}")
def delete_product(
    product_id:int,
    db:Session=Depends(get_db)
):
    existing = db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()

    db.delete(existing)
    db.commit()

    return {"message":"Product Deleted"}

@app.get("/search")
def search(
    keyword:str,
    db:Session=Depends(get_db)
):
    return db.query(models.Product).filter(
        models.Product.title.contains(keyword)
    ).all()

@app.get("/filter")
def filter_products(
    category:str,
    db:Session=Depends(get_db)
):
    return db.query(models.Product).filter(
        models.Product.category == category
    ).all()

@app.get("/dashboard")
def dashboard(db:Session=Depends(get_db)):

    total_users = db.query(models.User).count()

    total_products = db.query(models.Product).count()

    return {
        "total_users":total_users,
        "total_products":total_products
    }