import { useEffect, useState } from "react";
import API from "./api";

import ProductList from "./components/ProductList";
import ProductDetails from "./components/ProductDetails";


function App() {

    const [products, setProducts] = useState([]);
    const [selectedProduct, setSelectedProduct] = useState(null);


    useEffect(() => {

        API.get("/products")
            .then((response) => {
                setProducts(response.data);
            })
            .catch((error) => {
                console.log(error);
            });

    }, []);


    function getProductDetails(product_id) {

        API.get(`/products/${product_id}`)
            .then((response) => {
                setSelectedProduct(response.data);
            })
            .catch((error) => {
                console.log(error);
            });

    }


    return (
        <div>

            <h1>Products</h1>


            <ProductList
                products={products}
                getProductDetails={getProductDetails}
            />


            <ProductDetails
                product={selectedProduct}
            />

        </div>
    );
}


export default App;