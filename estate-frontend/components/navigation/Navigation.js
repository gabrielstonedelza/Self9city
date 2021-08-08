import { useState } from "react";
import Image from "next/image";
import Link from "next/link";
import styles from "../../styles/Navigation.module.css";
import Search from "../search/Search";
import { FaBars, FaChevronDown, FaTimes } from "react-icons/fa";

const Navigation = ({ children }) => {
  const [showMenu, setShowMenu] = useState(false);
  const [closeMenu, setCloseMenu] = useState(false);

  const handleOpenMenu = () => {
    setShowMenu(true);
    setCloseMenu(false);
  };
  const handleCloseMenu = () => {
    setCloseMenu(true);
    setShowMenu(false);
  };

  return (
    <>
      <nav className={styles.nav}>
        <ul>
          <li className={styles.logo}>
            <div className={styles.logotitle}>
              <Image
                src="/images/self-9.png"
                alt="logo"
                width={50}
                height={50}
              />
              <Link href="/">SELF9CITY</Link>
            </div>
          </li>
          <li className={styles.mybars}>
            <FaBars onClick={handleOpenMenu} />
          </li>
          <li className={styles.search}>
            <Search />
          </li>
          <div className={styles.notactive}>
            <div className={styles.navitems}>
              <li className={styles.cancelbtn}>
                <FaTimes onClick={handleCloseMenu} />
              </li>
              <li onClick={handleCloseMenu}>
                <Link href="/" className={styles.link}>
                  Home
                </Link>
              </li>

              <li onClick={handleCloseMenu}>
                <Link href="/about" className={styles.link}>
                  About
                </Link>
              </li>
            </div>
          </div>
          {showMenu ? (
            <div className={styles.items}>
              <li className={styles.cancelbtn}>
                <FaTimes onClick={handleCloseMenu} />
              </li>
              <li onClick={handleCloseMenu}>
                <Link href="/" className={styles.link}>
                  Home
                </Link>
              </li>
              <li onClick={handleCloseMenu}>
                <Link href="/about" className={styles.link}>
                  About
                </Link>
              </li>
            </div>
          ) : (
            closeMenu
          )}
        </ul>
      </nav>
      
      {/* <br /> */}
      {children}
    </>
  );
};

export default Navigation;
