
import { mount } from '@vue/test-utils'
import { beforeEach, afterEach, describe, it, expect, vi } from "vitest"
import createFetchMock from 'vitest-fetch-mock'
import BoatForm from './BoatForm.vue'
import BootstrapVue3 from 'bootstrap-vue-3'

const fetch = createFetchMock(vi)
fetch.enableMocks()
const global = {
  plugins: [BootstrapVue3],
}

describe('BoatForm', () => {
  beforeEach(() => {
    fetch.resetMocks()
  })
  afterEach(() => {
    vi.restoreAllMocks()
  })

  it('should set the name value if boat name provided', async () => {
    const boat = {
      name: 'Boaty McBoatface'
    }
    const wrapper = mount(BoatForm, {
      global,
      props: { boat },
    })
    expect(wrapper.find('input#name').element.value).toEqual(boat.name)
  })

  it('should set the name value to blank if boat name not provided', async () => {
    const boat = {}
    const wrapper = mount(BoatForm, {
      global,
      props: { boat },
    })
    expect(wrapper.find('input#name').element.value).toEqual('')
  })

  it('should create a new boat', async () => {
    fetch.mockResponseOnce(JSON.stringify({
      id: '123abc',
      swimlane_id: 'abc123',
      name: 'Boaty McBoatface',
      modified: '2022-09-18 20:22:48+0000',
    }))

    const boat = {
      swimlane_id: 'abc123'
    }
    const wrapper = mount(BoatForm, {
      global,
      props: { boat },
    })
    expect(wrapper.find('button[type=submit]').text()).toEqual('Create')
    wrapper.find('input#name').setValue('Boaty McBoatface')
    wrapper.find('form').trigger('submit')
    expect(wrapper.emitted()).toHaveProperty('submit')

    expect(fetch.mock.calls.length).toEqual(1);
    expect(fetch.mock.calls[0]).toEqual([
      'http://mock.server/boats/',
      {
        method: 'post',
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify({
          swimlane_id: 'abc123',
          name: 'Boaty McBoatface',
        })
      }
    ])
  })

  it('should update an existing boat', async () => {
    fetch.mockResponseOnce(JSON.stringify({
      id: '123abc',
      swimlane_id: 'abc123',
      name: 'Boaty McBoatface2',
      modified: '2022-09-18 20:22:48+0000',
    }))

    const boat = {
      id: '123abc',
      swimlane_id: 'abc123',
      name: 'Boaty McBoatface',
    }
    const wrapper = mount(BoatForm, {
      global,
      props: { boat },
    })
    expect(wrapper.find('button[type=submit]').text()).toEqual('Update')
    wrapper.find('input#name').setValue('Boaty McBoatface2')
    wrapper.find('form').trigger('submit')
    expect(wrapper.emitted()).toHaveProperty('submit')

    expect(fetch.mock.calls.length).toEqual(1);
    expect(fetch.mock.calls[0]).toEqual([
      'http://mock.server/boats/123abc/',
      {
        method: 'put',
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify({
          id: '123abc',
          swimlane_id: 'abc123',
          name: 'Boaty McBoatface2',
        })
      }
    ])
  })
})
