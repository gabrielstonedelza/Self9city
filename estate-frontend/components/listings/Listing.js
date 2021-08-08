import Link from 'next/link'
import Image from 'next/image'
import styles from '../../styles/Index.module.css'
import { FaCalendarAlt, FaShower, FaHome, FaEye } from "react-icons/fa";

const Listing = ({data}) => {
    return (
      <div className={styles.listingcontainer}>
        
        <Link
          href="/listing/[slug]"
          as={`/listing/${data.slug}`}
          passHref
          className={styles.listinglink}
        >
          <div className={styles.listingbox}>
            <Image
              width={300}
              height={200}
              src={data.get_listing_image}
              alt="listing image"
              // layout="responsive"
              className={styles.listingphoto}
            />
            <div className={styles.views}>
              <FaEye className={styles.eye} /> {data.views}
            </div>
            <div className={styles.listingdetails}>
              {/* listing type */}
              <span className={styles.listingtype}>{data.listing_type}</span>

              <h3>{data.price}</h3>
              <div className={styles.otherdetails}>
                <span>
                  <FaHome /> {data.rooms} |
                </span>
                <span>
                  <FaShower />
                  {data.baths} |
                </span>
                <span>{data.size_of_building}</span>
              </div>
              <br />
              <div className={styles.fulllocation}>{data.full_location}</div>
              <br />
            </div>
          </div>
        </Link>
        <br />
        <br />
      </div>
    );
}

export default Listing