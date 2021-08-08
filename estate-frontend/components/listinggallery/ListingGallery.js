import GalleryImages from "./GalleryImages";
import styles from '../../styles/Index.module.css'

const ListingGallery = ({ galleryListing }) => {
  return (
    <div className={styles.listinggallerycontainer}>
      {galleryListing.map((gallery) => (
        <GalleryImages gallery={gallery} key={gallery.id} />
      ))}
    </div>
  );
};

export default ListingGallery


