import styles from '../../styles/Showcase.module.css'

const Showcase = () => {
    return (
      <div>
        <div className={styles.showcase}>
          <div className={styles.showcaseback}></div>
          <div className={styles.showcaseoverlay}></div>
          <div className={styles.showcasecontents}>
            <h2>Discover your perfect home℠</h2>
            <p>
              With the most complete source of homes for sale & real estate near
              you
            </p>
            {/* <form>
              <input
                type="search"
                name=""
                id="search"
                placeholder="Address, School, City"
                size="70"
              />
            </form> */}
            <div>
              
            </div>
          </div>
        </div>
      </div>
    );
}

export default Showcase
