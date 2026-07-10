import { useEffect, useState } from "react";
import API from "./api";
import ProductList from "./components/ProductList";

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
            <ProductList products={products} />
        </div>
    );
}

export default App;