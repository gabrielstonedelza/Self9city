import { useState, useRef } from "react";
import { useRouter } from "next/router";
import Link from 'next/link'
import styles from '../../styles/Search.module.css'

const Search = ({}) => {
  const [searchTerm, setSearchTerm] = useState("");
  const [results, setResults] = useState([]);
  const [keyword, setKeyword] = useState("");
  const [isTyping,setIsTyping] = useState(false)
  const inputElement = useRef("");
  const [showResults,setShowResults] = useState(false)

  const searchHandler = async (e) => {

    setKeyword(inputElement.current.value);
    setSearchTerm(searchTerm);
    if(keyword.length > 0){
      setIsTyping(true)
      setShowResults(true)
    }

    if (keyword !== '' || keyword !== null) {

      const apiUrl = `http://127.0.0.1:8000/api/all_listings/?search=${keyword}`;
      const res = await fetch(apiUrl)
      const data = await res.json()
      setResults(data)
    }
  };

  const handleResultsBox = () =>{
    setShowResults(false)
  }

  return (
    <div className={styles.searchcontainer}>
      <form>
        <input
          type="search"
          placeholder="Search homes by their address"
          onChange={searchHandler}
          value={keyword}
          ref={inputElement}
        />
      </form>
      {
        showResults && <div className={styles.searchbox}>
          {results.map((result) => (
            
            <ul key={result.id}>
              <li onClick={handleResultsBox}>
                <Link href="/listing/[slug]"
                  as={`/listing/${result.slug}`}
                  passHref>
                  {result.full_location}
                </Link>
              </li>
            </ul>
          ))}
        </div> 
      }
    </div>
  );
};

export default Search;

