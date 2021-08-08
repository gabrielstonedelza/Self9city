import Listing from "./Listing"
import styles from '../../styles/Index.module.css'

const Listings = ({data}) => {
    return (
        <div className={styles.mainlisting}>
            {data.map(listing => (
                <Listing data={listing} key={listing.id}/>
            ))}
        </div>
    )
}

export default Listings
