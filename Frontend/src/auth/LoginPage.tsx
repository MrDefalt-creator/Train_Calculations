export default function LoginPage() {
    return (
        <div className="h-screen overflow-y-auto overflow-x-hidden flex justify-center
            items-center bg-blue-100">
            <div className="my-12 flex flex-col">
                <div className="flex flex-row justify-center py-16 px-12 bg-white rounded-2xl">
                    <div className="flex flex-col justify-center items-center">
                        <h2 className="font-medium font-sans text-2xl mb-8">
                            Добро пожаловать
                        </h2>
                        <div className="flex flex-col gap-4">
                            <input
                                placeholder="Логин"
                                required={true}
                                autoFocus={true}
                                autoComplete="username"
                                type="text"
                                className="w-full py-4 px-8 rounded-2xl border-2 border-gray-300
                                     outline-none
                                     focus:outline-none
                                     focus:border-blue-300
                                     focus:ring-0
                                     transition-colors"
                            />
                            <input
                                placeholder="Пароль"
                                required={true}
                                autoComplete="current-password"
                                type="password"
                                className="w-full py-4 px-8 rounded-2xl border-2 border-gray-300
                                     outline-none
                                     focus:outline-none
                                     focus:border-blue-300
                                     focus:ring-0
                                     transition-colors"
                            />
                        </div>

                    </div>
                </div>
            </div>
        </div>
    )
}