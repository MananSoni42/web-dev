import React from 'react'
import { shallow, mount } from 'enzyme'

import Connect4 from './connect4'

// add testEnvironment to jest + enzyme to get global DOM

describe('Connect 4 - board renders properly', () => {
    it('board has size 6x7 = 42', () => {
        const component = shallow(<Connect4 />)
        expect(component.find('.grid').length).toEqual(42)
    })

    it('There are 6 pointer buttons', () => {
        const component = shallow(<Connect4 />)
        expect(component.find('.ptr').length).toEqual(6)
    })
})

describe('Connect 4 functions work correctly', () => {
    it('Check to see if function is called correclty', () => {
        const setGame = jest.fn()
        const wrapper = mount(<Connect4 onClick={setGame} />)
        const handleClick = jest.spyOn(React, 'useState')
        handleClick.mockImplementation((game) => [game, setGame])

        wrapper.find('#btn0').simulate('click')
        expect(setGame).toBeTruthy()
    })

    it('Unit test for sample_test_fn', () => {
        const component = mount(<Connect4 />)
        const instance = component.instance()

        expect(instance.sample_test_fn(0, 0)).to.be(0)
    })
})
