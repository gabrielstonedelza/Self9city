import React, { useState } from 'react';
import FsLightbox from 'fslightbox-react';
import Image from 'next/image'
import styles from '../../styles/Index.module.css'
const GalleryImages = ({gallery}) => {
  const [toggler, setToggler] = useState(false);
    return (
      <>
        <FsLightbox
          toggler={toggler}
          initialAnimation="scale-in-long"
          slideChangeAnimation="scale-in"
          sources={[
            `${gallery.get_listings_image}`
          ]}
        />
        <Image
          src={gallery.get_listings_image}
          width={120}
          height={60}
          alt="gallery image"
          // layout="responsive"
          onClick={() => setToggler(!toggler)}
        />
      </>
    );
}

export default GalleryImages
