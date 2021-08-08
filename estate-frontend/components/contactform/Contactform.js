import { useState } from "react";
import { useRouter } from 'next/router'
import styles from "../../styles/Index.module.css";
import { ToastContainer, toast } from "react-toastify";
const Contactform = ({ slug }) => {
  const router = useRouter()
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  const [message, setMessage] = useState("");


  const handleContactForm = async (e) => {
    e.preventDefault();
    toast.success("Please wait,processing your data")
    const apiUrl = `http://64.227.22.163/api/contact_us/${slug}/`
    const res = await fetch(apiUrl, {
      body: JSON.stringify({
        listing: slug,
        full_name: name,
        email: email,
        phone: phone,
        message: message
      }),
      headers: {
        "Content-Type": "application/json"
      },
      method: "POST"
    })
    const results = await res.json()
    console.log(results)
    setTimeout(() => {
      router.push('/')
    }, 2000)

  };
  return (
    <div className={styles.myform}>
      <ToastContainer />
      <h3>Contact for more Information</h3>
      <form onSubmit={handleContactForm}>
        <div className={styles.formcontrol}>
          <label htmlFor="name">Name</label>
          <input
            required
            type="text"
            name=""
            id="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </div>
        <div className={styles.formcontrol}>
          <label htmlFor="email">Email</label>
          <input
            required
            type="text"
            name=""
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <div className={styles.formcontrol}>
          <label htmlFor="phone">Phone</label>
          <input
            required
            type="text"
            name="phone"
            id=""
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
          />
        </div>
        <div className={styles.formcontrol}>
          <label htmlFor="message">Message</label>
          <input
            required
            type="text"
            name=""
            id="message"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />
        </div>
        <br />
        <div className={styles.formcontrol}>
          <button type="submit">Send</button>
        </div>
        <br />
        <div className={styles.formcontrol}>By proceeding, you consent to receive calls and texts at the number and email  you provided.Please make sure all the information provided are valid.
        </div>
      </form>
    </div>
  );
};

export default Contactform;
