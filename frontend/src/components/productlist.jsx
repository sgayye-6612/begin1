import ProductCard from "./ProductCard";

function ProductList({ products }) {

    return (
        <div className="products-container">

            {products.map((product) => (
                <ProductCard
                    key={product.product_id}
                    product={product}
                />
            ))}

        </div>
    );
}

export default ProductList;