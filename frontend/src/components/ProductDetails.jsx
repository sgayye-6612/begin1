function ProductDetails({ product }) {

    if (!product) {
        return null;
    }

    return (
        <div>

            <h2>Product Details</h2>

            <h3>{product.name}</h3>

            <p>
                Price: ${product.price}
            </p>

            <p>
                Category ID: {product.category_id}
            </p>

            <p>
                Subcategory ID: {product.subcategory_id}
            </p>

        </div>
    );
}

export default ProductDetails;