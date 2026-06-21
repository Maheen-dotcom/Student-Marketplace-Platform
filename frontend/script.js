const API_URL = "https://student-marketplace-platform-production.up.railway.app";

async function registerUser() {

    const full_name =
    document.getElementById("reg_name").value;

    const email =
    document.getElementById("reg_email").value;

    const password =
    document.getElementById("reg_password").value;

    const response = await fetch(
        `${API_URL}/register`,
        {
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({
                full_name:full_name,
                email:email,
                password:password,
                phone:"03000000000",
                role:"Student"
            })
        }
    );

    const data = await response.json();

    alert(data.message || data.detail);
}

async function loginUser() {

    const email =
    document.getElementById("login_email").value;

    const password =
    document.getElementById("login_password").value;

    const response = await fetch(
        `${API_URL}/login`,
        {
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({
                email:email,
                password:password
            })
        }
    );

    const data = await response.json();

    alert(data.message || data.detail);
}

async function addProduct() {

    const title =
    document.getElementById("title").value;

    const description =
    document.getElementById("description").value;

    const category =
    document.getElementById("category").value;

    const price =
    document.getElementById("price").value;

    const seller =
    document.getElementById("seller").value;

    const response = await fetch(
        `${API_URL}/products`,
        {
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({
                title:title,
                description:description,
                category:category,
                price:parseFloat(price),
                seller_name:seller
            })
        }
    );

    const data = await response.json();

    alert(data.message);
}

async function loadProducts(){

    const response =
    await fetch(`${API_URL}/products`);

    const products =
    await response.json();

    let html = "";

    products.forEach(product=>{

        html += `
<div class="card">

<h2>${product.title}</h2>

<p>${product.description}</p>

<p><strong>Category:</strong> ${product.category}</p>

<p><strong>Price:</strong> PKR ${product.price}</p>

<p><strong>Seller:</strong> ${product.seller_name}</p>

</div>
`;
    });

    const container =
    document.getElementById("productList");

    if(container){
        container.innerHTML = html;
    }
}

async function loadDashboard(){

    const response =
    await fetch(`${API_URL}/dashboard`);

    const data =
    await response.json();

    const users =
    document.getElementById("totalUsers");

    const products =
    document.getElementById("totalProducts");

    if(users){
        users.innerText =
        data.total_users;
    }

    if(products){
        products.innerText =
        data.total_products;
    }
}

loadProducts();
loadDashboard();