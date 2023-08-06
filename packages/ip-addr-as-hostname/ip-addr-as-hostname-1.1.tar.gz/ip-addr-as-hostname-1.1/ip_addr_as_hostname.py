import asyncio
import re

import dns.exception
import dns.message
import dns.opcode
import dns.query
import dns.rcode
import dns.rdatatype
import dns.rdtypes.IN.A
import dns.rrset


class IpAddrAsHostnameProtocol(asyncio.DatagramProtocol):
    __ADDRESS_REGEX = re.compile('(\d+.\d+.\d+.\d+).ip.addr.as.hostname')

    def __init__(self):
        self.transport: asyncio.DatagramTransport = None

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        query: dns.message.Message = dns.message.from_wire(data)

        if query.opcode() != dns.opcode.QUERY:
            self.transport.sendto(self.__error(query, dns.rcode.FORMERR), addr)
            return

        if len(query.question) == 0 or len(query.question) > 1:
            self.transport.sendto(self.__error(query, dns.rcode.FORMERR), addr)
            return

        question: dns.rrset.RRset = query.question[0]
        if question.rdclass != dns.rdatatype.A:
            self.transport.sendto(self.__error(query, dns.rcode.NOTIMP), addr)
            return

        match = self.__ADDRESS_REGEX.match(str(question.name))
        if not match:
            self.transport.sendto(self.__error(query, dns.rcode.NXDOMAIN), addr)
            return

        try:
            rdata = dns.rdtypes.IN.A.A(question.rdclass, question.rdtype, match.group(1))
        except dns.exception.SyntaxError:
            self.transport.sendto(self.__error(query, dns.rcode.NXDOMAIN), addr)
            return

        rrset = dns.rrset.from_rdata(question.name, 600, rdata)

        response = dns.message.make_response(query, recursion_available=True)
        response.set_rcode(dns.rcode.NOERROR)
        response.answer.append(rrset)
        self.transport.sendto(response.to_wire(), addr)

    # noinspection PyMethodMayBeStatic
    def __error(self, query, rcode):
        response = dns.message.make_response(query, recursion_available=True)
        response.set_rcode(rcode)
        return response.to_wire()


async def create_transport() -> asyncio.BaseTransport:
    loop = asyncio.get_event_loop()
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: IpAddrAsHostnameProtocol(),
        local_addr=('127.0.0.1', 15353)
    )
    return transport


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    transport: asyncio.BaseTransport = loop.run_until_complete(create_transport())
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print("exit")
    finally:
        transport.close()
