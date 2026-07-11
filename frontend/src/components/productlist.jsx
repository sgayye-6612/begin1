import ProductCard from "./ProductCard";


function ProductList({ products, getProductDetails }) {

    return (
        <div>

            {products.map((product) => (

                <ProductCard
                    key={product.product_id}
                    product={product}
                    getProductDetails={getProductDetails}
                />

            ))}

        </div>
    );
}


export default ProductList;
