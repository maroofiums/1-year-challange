import gsap from "gsap";
import { useEffect, useRef } from "react";

const ContactForm = () =>{
    const box = useRef();
    useEffect(()=>{
        gsap.from(box.current,{
            opacity:0,
            y:50,
            duration:1,
            ease:"power2.out",
        });
    },[]);

    return (
        <div className="page">
            <div ref={box}>
                <h1>📞 Contact Page</h1>
                <p>This is the homepage animated by GSAP.</p>
            </div>
        </div>
    )
}

export default ContactForm;
