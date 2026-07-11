function ProductCard({ product, getProductDetails }) {

    return (
        <div className="product-card">

            <h3>{product.name}</h3>




            <button onClick={() => getProductDetails(product.product_id)}>
                View Details
            </button>

        </div>
    );
}


export default ProductCard;