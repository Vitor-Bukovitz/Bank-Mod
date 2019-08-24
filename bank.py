class Banco: 
    def novo_cliente(self):  
        nome = input("Name: ")  
        ssn = input("SSN: ")  
        conta = input("Type of account:\n 1- Salary\n 2- Comum\n 3- Plus\n")  
        value = float(input("---Use (.) for decimal separations---\nInitial value: "))  
        password = input("Password: \n")  
        arquivo = open("%s.txt" % ssn, "w")  
        if conta == "1": 
            lista_salario = [str(nome), str(ssn), "Salary", str(value), str(password)]
            for ele in lista_salario: 
                arquivo.write(ele+'\n')  
        elif conta == "2": 
            lista_comum = [str(nome), str(ssn), "Comum", str(value), str(password)]
            for ele in lista_comum: 
                arquivo.write(ele+'\n')  
        elif conta == "3": 
            lista_plus = [str(nome), str(ssn), "Plus", str(value), str(password)]
            for ele in lista_plus: 
                arquivo.write(ele+'\n')  
        else: 
            print("Invalid command")  
        arquivo.close()  

    def apaga_cliente(self):  
        import os  
        ssn = input("SSN number of the client to delete: ")  
        if os.path.exists("%s.txt" % ssn):  
            while True:  
                pergunta = int(input("Delete client?\n1 - Yes\n2 - No\n"))  
                if pergunta == 1:  
                    try: 
                        os.remove("%s.txt" % ssn)  
                        os.remove("%s_Extract.txt" % ssn) 
                        print("Client deleted") 
                        break  
                    except Exception: 
                        break    
                elif pergunta == 1:  
                    break  
                else: 
                    continue  
        else:  
            print("Client is not registered") 
    
    def debita(self): 
        resultado = 0 
        ssn = input("SSN: ") 
        import os 
        if os.path.exists("%s.txt" % ssn): 
            arquivo = open("%s.txt" % ssn, "r") 
            lines_arquivo = arquivo.readlines() 
            arquivo.close()  
            if lines_arquivo[2] == "Salary\n": 
                while True:       
                    password = input("Password: ") 
                    password = password + "\n" 
                    if password == lines_arquivo[4]: 
                        value = float(input("---Use (.) for decimal separations---\nvalue: ")) 
                        value = round(value,2) 
                        Rate = round((value*0.05), 2) 
                        resultado = round(float(lines_arquivo[-2]) - float(value) - Rate, 2) 
                        if resultado >= 0: 
                            lines_arquivo[-2] = str(round(resultado, 2)) + '\n' 
                            arquivo = open("%s.txt" % ssn, "w") 
                            arquivo.writelines(lines_arquivo) 
                            arquivo.close() 
                            print("\nDebit realized\n") 
                            operador = "   -   " 
                            resultado_total = operador + str(value) 
                            self.armazenar_Extract(ssn, resultado_total) 
                            break 
                        else: 
                            print("\nDebit limit exceeded\n") 
                            break 
                    else: 
                        print("Incorrect password") 

            if lines_arquivo[2] == "Comum\n": 
                while True:       
                    password = input("Password: ") 
                    password = password + "\n" 
                    if password == lines_arquivo[4]: 
                        value = float(input("---Use (.) for decimal separations---\nValue: ")) 
                        value = round(value,2) 
                        Rate = round((value*0.03), 2) 
                        resultado = round(float(lines_arquivo[-2]) - float(value) - Rate, 2) 
                        if resultado >= -500: 
                            lines_arquivo[-2] = str(round(resultado,2 )) + "\n" 
                            arquivo = open("%s.txt" % ssn, "w") 
                            arquivo.writelines(lines_arquivo) 
                            arquivo.close() 
                            print("\nDebit realized\n") 
                            operador = "   -   " 
                            resultado_total = operador + str(value) 
                            self.armazenar_Extract(ssn, resultado_total) 
                            break 
                        else: 
                            print("\nDebit limit exceeded\n") 
                            break 
                    else: 
                        print("Incorrect password") 
                    
            if lines_arquivo[2] == "Plus\n": 
                while True: 
                    password = input("Password: ") 
                    password = password + "\n" 
                    if password == lines_arquivo[-1]: 
                        value = float(input('---Use (.) for decimal separations---\nvalue: ')) 
                        value = round(value, 2) 
                        Rate = round((value*0.01), 2) 
                        resultado = round(float(lines_arquivo[-2]) - float(value) - Rate, 2) 
                        if resultado >= -5000: 
                            lines_arquivo[-2] = str(round(resultado, 2)) + "\n" 
                            arquivo = open("%s.txt" % ssn, "w") 
                            arquivo.writelines(lines_arquivo) 
                            arquivo.close() 
                            print("\nDebit realized\n") 
                            operador = "   -   " 
                            resultado_total = operador + str(value) 
                            self.armazenar_Extract(ssn, resultado_total) 
                            break 
                        else: 
                            print("\nDebit limit exceeded\n") 
                            break 
                    else: 
                        print("Incorrect password") 
        else: 
            print("\nIncorrect SSN\n")
    

    def deposita(self): 
        resultado = 0 
        ssn = input("SSN: ") 
        import os 
        if os.path.exists("%s.txt" % ssn): 
            arquivo = open("%s.txt" % ssn) 
            lines_arquivo = arquivo.readlines() 
            arquivo.close() 

            while True: 
                value = float(input("---Use (.) for decimal separations---\nvalue: ")) 
                resultado = round(float(lines_arquivo[-2])+ float(value), 2) 
                lines_arquivo[-2] = str(round(resultado,2 )) + "\n" 
                arquivo = open("%s.txt" % ssn, "w") 
                arquivo.writelines(lines_arquivo) 
                arquivo.close() 
                print("\nDeposit completed\n") 
                operador = "   +   " 
                resultado = operador + str(value) 
                self.armazenar_Extract(ssn, resultado) 
                break 
        else: 
            print("\nClient is not registered\n") 


    def Balance(self): 
        ssn = input("SSN: ") 
        import os 
        if os.path.exists("%s.txt" % ssn): 
            password = input("Password: ") 
            arquivo = open("%s.txt" % ssn, "r") 
            lines_arquivo = arquivo.readlines() 
            arquivo.close() 
            if password + "\n" == lines_arquivo[-1]: 
                print("\n Balance:R$ %s \n" % lines_arquivo[-2]) 
            else: 
                print("Incorrect password") 
        else: 
            print("Client is not registered") 



    def Extract(self): 
        import os 
        ssn = input("SSN: ") 
        if os.path.exists("%s.txt" % ssn): 
            password = input("Password: ") 
            arquivo = open("%s.txt" % ssn) 
            lines_arquivo = arquivo.readlines() 
            arquivo.close() 
            if password + "\n" == lines_arquivo[-1]: 
                nome = lines_arquivo[0] 
                nome = nome.replace("\n", "") 
                conta = lines_arquivo[2] 
                conta = conta.replace("\n", "") 
                arquivo_Extract = open("%s_Extract.txt" % ssn) 
                print("\n\n---------------Extract---------------") 
                print("Name: " + nome) 
                print("\nSSN: " + ssn) 
                print("\nAccount: " + conta) 
                arquivo_Extract = arquivo_Extract.readlines() 
                for line in arquivo_Extract: 
                    print(line) 
                arquivo.close() 
                print("\n-------------------------------------\n\n") 
            else: 
                print("\n\nPassword Invalid\n\n")
        else: 
            print("\n\nClient not signed up\n\n")




    def armazenar_Extract(self, ssn, value): 
        import os 
        from time import gmtime, strftime, sleep 
        data = strftime("%d-%m-%Y %H:%M:%S") 
        data = str(data) 
        arquivo = open("%s.txt" % ssn) 
        lines_arquivo = arquivo.readlines() 
        arquivo.close() 
        value = str(value) 
        Balance = lines_arquivo[3] 
        Balance = str(Balance) 
        Balance = Balance.replace('\n', '') 
        if lines_arquivo[2] == "Comum\n": 
            comum_Rate = "0.03"
            arquivo_Extract = open("%s_Extract.txt" % ssn, "a")
            arquivo_Extract.write("\nDate:  " + data + value + "     Balance:  " + Balance + "     Rate:  " + comum_Rate)
            arquivo_Extract.close()
        elif lines_arquivo[2] == "Plus\n":
            plus_Rate = "0.01"
            arquivo_Extract = open("%s_Extract.txt" % ssn, "a")
            arquivo_Extract.write("\nDate:  " + data + value + "     Balance:  " + Balance + "     Rate:  " + plus_Rate)
            arquivo_Extract.close()
        elif lines_arquivo[2] == "Salary\n":
            salario_Rate = "0.05"
            arquivo_Extract = open("%s_Extract.txt" % ssn, "a")
            arquivo_Extract.write("\nDate:  " + data + value + "     Balance:  " + Balance + "     Rate:  " + salario_Rate)
            arquivo_Extract.close()


    def start(self):
        while True:
            menu = input(("1- New Client\n2- Delete client\n3- Debit\n4- Deposit\n5- Balance\n6- Extract\n\n\n0- Exit\n"))
            if menu == "1":
                self.novo_cliente()
            elif menu =="2":
                self.apaga_cliente()
            elif menu == "3":
                self.debita()
            elif menu == "4":
                self.deposita()
            elif menu == "5":
                self.Balance()
            elif menu == "6":
                self.Extract()
            elif menu == "0":
                break
            else:
                continue




my_bank = Banco()
my_bank.start()
