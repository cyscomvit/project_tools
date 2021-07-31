import main
import input

r = input.response

if r == '1':
    main.synack_scan()
elif r == '2':
    main.udp_scan()
elif r == '3':
    main.comp_scan()
elif r == '4':
    main.reg_scan()

elif r == '5':
    main.ping_scan()
