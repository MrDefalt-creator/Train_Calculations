import {motion} from "motion/react"
import {useState} from "react";


export default function LoginPage() {
    const [hidden, setHidden] = useState(true)
    const [login, setLogin] = useState("")
    const [password, setPassword] = useState("")


    return (
        <div className="h-screen overflow-y-auto overflow-x-hidden flex justify-center
            items-center bg-blue-100 p-4">
            <div className="w-full max-w-md min-w-100">
                <div className="flex flex-col items-center py-16 px-12 bg-white rounded-2xl w-full">
                    <h2 className="font-medium font-sans text-3xl mb-8">
                        Добро пожаловать
                    </h2>
                    <div className="flex flex-col gap-4 w-full justify-center items-center">
                        <input
                            value={login}
                            onChange={(e) => setLogin(e.target.value)}
                            placeholder="Логин"
                            required={true}
                            autoFocus={true}
                            autoComplete="username"
                            type="text"
                            className="w-full py-3 px-8 rounded-2xl border-2 border-gray-300
                                 outline-none
                                 bg-gray-50
                                 focus:outline-none
                                 focus:border-blue-300
                                 focus:ring-0
                                 focus:bg-blue-50
                                 transition-colors"
                        />
                        <div className="flex flex-row w-full justify-center items-center relative">
                            <input
                                value={password}
                                onChange={e => setPassword(e.target.value)}
                                placeholder="Пароль"
                                required={true}
                                autoComplete="current-password"
                                type={hidden ? "password":"text"}
                                className="w-full py-3 px-8 rounded-2xl border-2 border-gray-300
                                    outline-none
                                    bg-gray-50
                                    focus:outline-none
                                    focus:border-blue-300
                                    focus:ring-0
                                    focus:bg-blue-50
                                    transition-colors
                                    relative"

                            />
                            <img src="/open-eye.png" height="20px" width="20px" className={`cursor-pointer absolute ${hidden ? "hidden" : ""}`} onClick={() => setHidden(!hidden)} style={{right: "10px"}}/>
                            <img src="/closed-eye.png" height="20px" width="20px" className={`cursor-pointer absolute ${hidden ? "" : "hidden"}`} onClick={() => setHidden(!hidden)} style={{right: "10px"}}/>
                        </div>

                        <motion.button className=""
                                       initial={{width: "100%", color: "oklch(80.9% 0.105 251.813)"}}
                                       whileHover={{width: "90%", color: "oklch(62.3% 0.214 259.815)"}}
                                       transition={{duration: 0.4, ease: "easeInOut"}}
                        >
                            <button className="w-full py-3 rounded-2xl text-white bg-blue-300">Войти</button>
                        </motion.button>

                    </div>
                </div>
            </div>
        </div>
    )
}