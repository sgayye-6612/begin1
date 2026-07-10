import { useEffect, useState } from "react";
import API from "./api";

function App() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    API.get("/products")
      .then((response) => {
        setProducts(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      <h1>Products</h1>

      {products.map((product) => (
  <div key={product.product_id}>
    <h3>{product.name}</h3>
    <p>Price: ${product.price}</p>
  </div>
))}
    </div>
  );
}

export default App;